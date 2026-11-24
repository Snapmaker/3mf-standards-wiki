#!/usr/bin/env python3
"""Build index/field_dictionary.json from tools/kb_index/field_dictionary.csv.

The field dictionary is the machine-readable companion to the 3MF engineering
specification, Appendix D.  It records, for every key known to the v0
reconciliation (817 entries):

  * the serialized key name and its alias relation,
  * the target file (currently project_settings.config),
  * the logical value type,
  * the static default status/value,
  * the whitelist/ban category,
  * whether the key was observed in the sample set, and
  * the approval status (pending / pending_review / banned_draft / approved).

Two booleans are deliberately separate:

  * sample_observed  -- the key occurred in the seven sample files;
  * approval        -- the key is approved for writing.

Sample presence is NOT approval.  Only approval == "approved" may be used as
a normative whitelist entry; the current snapshot is draft, so the 584
candidates remain "pending" until maintainers confirm them.

The source CSV is maintainer-edited.  ``--import-v0`` is a one-way bootstrap
from the internal v0 reconciliation (docs/data/, not published) and should
only be used when re-importing that snapshot, not for routine edits.

Usage:
  python tools/kb_index/build_field_dictionary.py
  python tools/kb_index/build_field_dictionary.py --check
  python tools/kb_index/build_field_dictionary.py --import-v0   # internal

Exit codes: 0 success, 1 validation failure / stale artefact.
"""

from __future__ import annotations

import argparse
import csv
import difflib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE_CSV = ROOT / 'tools' / 'kb_index' / 'field_dictionary.csv'
OUT_PATH = ROOT / 'index' / 'field_dictionary.json'
V0_CSV = ROOT / 'docs' / 'data' / 'field-dictionary-project-settings-v0.csv'
METADATA_JSON = ROOT / 'docs' / 'data' / 'print_config_metadata.json'
SETTINGS_ROOT = ROOT / 'wiki' / 'settings'

# Dataset-level facts.  Sample versions come from the v0 sample inventory
# (docs/01 section 1); update them when the sample set changes.
SAMPLE_VERSIONS = ('2.3.6', '2.4.0')
SOURCE_SNAPSHOT = 'v0 field-dictionary reconciliation (786 static definitions x 584 observed keys)'
REFERENCES = {
    'spec': 'wiki/specification/3mf/3mf_standard.md',
    'sections': [
        {
            'title': '6.3 全量配置快照：Metadata/project_settings.config',
            'anchor': '63-全量配置快照metadataproject_settingsconfig',
        },
        {'title': '8.1 生产者要求', 'anchor': '81-生产者要求'},
        {
            'title': '附录 D（规范性）字段字典与写入白名单',
            'anchor': '附录-d规范性字段字典与写入白名单',
        },
    ],
}

COLUMNS = [
    'key',
    'alias_of',
    'alias_kind',
    'file',
    'type',
    'default_status',
    'default_value',
    'category',
    'category_label',
    'sample_observed',
    'source_defined',
    'definition_source',
    'observed_versions',
    'applicable_versions',
    'approval',
    'approval_note',
    'note',
]

CATEGORY_LABELS = {
    'whitelist_candidate': '落盘字段',
    'banned_sla': 'SLA树脂流程专用',
    'banned_cli': 'CLI动作参数',
    'banned_runtime': '运行时派生状态',
    'banned_gui_deprecated': 'GUI内部/废弃候选',
    'banned_preset_internal': '预设系统内部',
    'banned_host_credentials': '打印主机连接（凭据）',
}

V0_CATEGORY_MAP = {
    '落盘字段': 'whitelist_candidate',
    'SLA树脂流程专用': 'banned_sla',
    'CLI动作参数': 'banned_cli',
    '运行时派生状态': 'banned_runtime',
    'GUI内部/废弃候选': 'banned_gui_deprecated',
    '预设系统内部': 'banned_preset_internal',
    '打印主机连接': 'banned_host_credentials',
}

ALIAS_KINDS = ('legacy_prefix', 'macro_declared', 'schema_version')
DEFINITION_SOURCES = ('static', 'derived', 'macro', 'runtime', 'unknown')
APPROVALS = ('pending', 'pending_review', 'banned_draft', 'approved', 'rejected')
DEFAULT_STATUSES = ('static', 'empty', 'none', 'unknown')
FILES = ('project_settings.config',)

TYPE_BASE = {
    'coBool': 'Boolean',
    'coInt': 'Integer',
    'coFloat': 'Float',
    'coFloatOrPercent': 'Float or Percentage',
    'coPercent': 'Percentage',
    'coString': 'Text',
    'coEnum': 'Choice',
    'coPoint': 'Point',
    'coPoint3': 'Point 3D',
    'coNone': 'Unknown',
}
TYPE_LIST = {
    'coBools': 'Boolean list',
    'coInts': 'Integer list',
    'coFloats': 'Float list',
    'coFloatsOrPercents': 'Float or Percentage list',
    'coPercents': 'Percentage list',
    'coStrings': 'Text list',
    'coEnums': 'Choice list',
    'coPoints': 'Point list',
    'coPoint3s': 'Point 3D list',
}
LOGICAL_TYPES = frozenset(TYPE_BASE.values()) | frozenset(TYPE_LIST.values())

# 2.4.0 sample additions (docs/01 section 3.3); project_schema_version is one
# of the eight and is also the only runtime schema field in the 31.
V204_FIELDS = frozenset({
    'filament_flow_step_size',
    'filament_flow_support',
    'filament_grouping_mode',
    'filament_volume_type',
    'nozzle_volume_type',
    'printer_flow_support',
    'process_flow_support',
    'project_schema_version',
})

KEY_RE = re.compile(r'^[A-Za-z0-9_]+$')
VERSION_RE = re.compile(r'^\d+(?:\.\d+){1,3}$')


class DictionaryError(Exception):
    """Validation or build error with a maintainer-facing message."""


@dataclass(frozen=True)
class FieldRecord:
    key: str
    alias_of: str
    alias_kind: str
    file: str
    value_type: str
    default_status: str
    default_value: str
    category: str
    category_label: str
    sample_observed: bool
    source_defined: bool
    definition_source: str
    observed_versions: tuple[str, ...]
    applicable_versions: tuple[str, ...]
    approval: str
    approval_note: str
    note: str


def logical_type(cotype: str) -> str:
    """Map a PrintConfig type name to the wiki's logical type label."""
    cotype = (cotype or '').strip()
    if not cotype:
        return 'Unknown'
    if cotype.startswith('ConfigOptionEnum<') or cotype.startswith('coEnum<'):
        return 'Choice'
    if cotype.startswith('ConfigOption'):
        cotype = 'co' + cotype[len('ConfigOption'):]
    return TYPE_BASE.get(cotype) or TYPE_LIST.get(cotype) or 'Unknown'


def parse_bool(value: str, field: str, line: int) -> bool:
    if value == 'true':
        return True
    if value == 'false':
        return False
    raise DictionaryError(f'line {line}: {field} must be true/false, got {value!r}')


def parse_versions(value: str, field: str, line: int) -> tuple[str, ...]:
    if not value:
        return ()
    parts = [p.strip() for p in value.split(';')]
    if any(not p for p in parts):
        raise DictionaryError(f'line {line}: {field} contains an empty version')
    for part in parts:
        if not VERSION_RE.fullmatch(part):
            raise DictionaryError(f'line {line}: {field} has invalid version {part!r}')
    return tuple(dict.fromkeys(parts))


def parse_row(row: dict[str, str], line: int) -> FieldRecord:
    missing = [c for c in COLUMNS if c not in row]
    if missing:
        raise DictionaryError(f'line {line}: missing columns: {", ".join(missing)}')
    raw = {c: row[c] if row[c] is not None else '' for c in COLUMNS}
    # default_value may legitimately be a single space (e.g. filament_end_gcode);
    # strip only the metadata fields, never the value itself.
    values = {c: raw[c].strip() for c in COLUMNS if c != 'default_value'}
    values['default_value'] = raw['default_value']

    key = values['key']
    if not KEY_RE.fullmatch(key):
        raise DictionaryError(f'line {line}: invalid key {key!r}')

    alias_of = values['alias_of']
    if alias_of and not KEY_RE.fullmatch(alias_of):
        raise DictionaryError(f'line {line}: invalid alias_of {alias_of!r}')
    alias_kind = values['alias_kind']
    if alias_kind and alias_kind not in ALIAS_KINDS:
        raise DictionaryError(f'line {line}: invalid alias_kind {alias_kind!r}')
    definition_source = values['definition_source']
    if definition_source not in DEFINITION_SOURCES:
        raise DictionaryError(
            f'line {line}: invalid definition_source {definition_source!r}')

    file_name = values['file']
    if file_name not in FILES:
        raise DictionaryError(f'line {line}: invalid file {file_name!r}')
    value_type = values['type']
    if value_type not in LOGICAL_TYPES:
        raise DictionaryError(f'line {line}: invalid type {value_type!r}')

    default_status = values['default_status']
    if default_status not in DEFAULT_STATUSES:
        raise DictionaryError(f'line {line}: invalid default_status {default_status!r}')
    default_value = values['default_value']
    if default_status == 'static' and not default_value:
        raise DictionaryError(
            f'line {line}: default_value is required for default_status=static')
    if default_status != 'static' and default_value:
        raise DictionaryError(
            f'line {line}: default_value must be empty for default_status={default_status}')

    category = values['category']
    if category not in CATEGORY_LABELS:
        raise DictionaryError(f'line {line}: invalid category {category!r}')
    if values['category_label'] != CATEGORY_LABELS[category]:
        raise DictionaryError(
            f'line {line}: category_label {values["category_label"]!r} does not match '
            f'category {category!r}')

    approval = values['approval']
    if approval not in APPROVALS:
        raise DictionaryError(f'line {line}: invalid approval {approval!r}')

    sample_observed = parse_bool(values['sample_observed'], 'sample_observed', line)
    source_defined = parse_bool(values['source_defined'], 'source_defined', line)
    observed_versions = parse_versions(values['observed_versions'], 'observed_versions', line)
    applicable_versions = parse_versions(
        values['applicable_versions'], 'applicable_versions', line)

    return FieldRecord(
        key=key,
        alias_of=alias_of,
        alias_kind=alias_kind,
        file=file_name,
        value_type=value_type,
        default_status=default_status,
        default_value=default_value,
        category=category,
        category_label=values['category_label'],
        sample_observed=sample_observed,
        source_defined=source_defined,
        definition_source=definition_source,
        observed_versions=observed_versions,
        applicable_versions=applicable_versions,
        approval=approval,
        approval_note=values['approval_note'],
        note=values['note'],
    )


def validate_records(records: list[FieldRecord]) -> None:
    """Cross-record and cross-field checks applied to the CSV and to imports."""
    seen: set[str] = set()
    dupes: list[str] = []
    for r in records:
        if r.key in seen:
            dupes.append(r.key)
        seen.add(r.key)
    if dupes:
        raise DictionaryError('duplicate keys: ' + ', '.join(sorted(dupes)))
    keys = seen

    for r in records:
        where = f'key {r.key}'
        if r.sample_observed != (r.category == 'whitelist_candidate'):
            raise DictionaryError(
                f'{where}: sample_observed must be true exactly for whitelist_candidate')

        if r.category == 'whitelist_candidate':
            if r.approval not in ('pending', 'approved'):
                raise DictionaryError(
                    f'{where}: whitelist_candidate approval must be pending/approved')
        elif r.category == 'banned_gui_deprecated':
            if r.approval != 'pending_review':
                raise DictionaryError(
                    f'{where}: banned_gui_deprecated approval must be pending_review')
        elif r.approval not in ('banned_draft', 'rejected'):
            raise DictionaryError(
                f'{where}: banned category approval must be banned_draft/rejected')

        if r.alias_kind == 'legacy_prefix':
            if not r.alias_of:
                raise DictionaryError(f'{where}: legacy_prefix requires alias_of')
            if r.definition_source != 'derived':
                raise DictionaryError(f'{where}: legacy_prefix requires definition_source=derived')
        elif r.alias_kind == 'macro_declared':
            if r.alias_of:
                raise DictionaryError(f'{where}: macro_declared must not set alias_of')
            if r.definition_source != 'macro':
                raise DictionaryError(f'{where}: macro_declared requires definition_source=macro')
        elif r.alias_kind == 'schema_version':
            if r.alias_of:
                raise DictionaryError(f'{where}: schema_version must not set alias_of')
            if r.definition_source != 'runtime':
                raise DictionaryError(f'{where}: schema_version requires definition_source=runtime')
        elif r.alias_of:
            raise DictionaryError(f'{where}: alias_of requires alias_kind')

        if r.definition_source == 'derived' and not r.alias_of:
            raise DictionaryError(f'{where}: derived definition requires alias_of')
        if r.definition_source == 'runtime' and r.alias_kind != 'schema_version':
            raise DictionaryError(f'{where}: runtime definition requires schema_version')
        if r.definition_source == 'static' and r.alias_kind:
            raise DictionaryError(f'{where}: static definition cannot have alias_kind')

        if r.approval == 'approved':
            if not r.sample_observed:
                raise DictionaryError(f'{where}: approved key must be sample_observed')
            if not r.applicable_versions:
                raise DictionaryError(
                    f'{where}: approved key needs applicable_versions')

    for r in records:
        if r.alias_of and r.alias_of not in keys:
            raise DictionaryError(f'key {r.key}: alias_of target {r.alias_of!r} not in dictionary')


def read_source(path: Path) -> list[FieldRecord]:
    if not path.is_file():
        raise DictionaryError(f'source CSV not found: {path}')
    with open(path, encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != COLUMNS:
            raise DictionaryError(
                'source CSV header does not match expected columns:\n'
                f'  expected: {", ".join(COLUMNS)}\n'
                f'  actual:   {", ".join(reader.fieldnames or [])}')
        records: list[FieldRecord] = []
        for line, row in enumerate(reader, start=2):
            if None in row:
                raise DictionaryError(f'line {line}: too many fields')
            if any(value is None for value in row.values()):
                raise DictionaryError(f'line {line}: too few fields')
            records.append(parse_row(row, line))
    validate_records(records)
    return records


def write_source(path: Path, records: list[FieldRecord]) -> None:
    records = sorted(records, key=lambda r: (r.key.lower(), r.key))
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS, lineterminator='\n')
        writer.writeheader()
        for r in records:
            writer.writerow(record_to_row(r))


def record_to_row(r: FieldRecord) -> dict[str, str]:
    return {
        'key': r.key,
        'alias_of': r.alias_of,
        'alias_kind': r.alias_kind,
        'file': r.file,
        'type': r.value_type,
        'default_status': r.default_status,
        'default_value': r.default_value,
        'category': r.category,
        'category_label': r.category_label,
        'sample_observed': 'true' if r.sample_observed else 'false',
        'source_defined': 'true' if r.source_defined else 'false',
        'definition_source': r.definition_source,
        'observed_versions': ';'.join(r.observed_versions),
        'applicable_versions': ';'.join(r.applicable_versions),
        'approval': r.approval,
        'approval_note': r.approval_note,
        'note': r.note,
    }


def load_pages() -> dict[str, str]:
    """Map lower-case key stems to repo-relative page paths."""
    pages: dict[str, str] = {}
    for path in sorted(SETTINGS_ROOT.glob('*/*/*.md')):
        if path.stem.endswith('_overview'):
            continue
        stem = path.stem.lower()
        if stem in pages:
            raise DictionaryError(
                f'case-insensitive page stem collision: {pages[stem]} / {path}')
        pages[stem] = path.relative_to(ROOT).as_posix()
    return pages


def display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def default_json_value(r: FieldRecord) -> str | None:
    if r.default_status == 'static':
        return r.default_value
    if r.default_status == 'empty':
        return ''
    return None


def build_artifact(records: list[FieldRecord], pages: dict[str, str]) -> dict:
    ordered = sorted(records, key=lambda r: (r.key.lower(), r.key))
    entries = []
    for r in ordered:
        entry = {
            'key': r.key,
            'alias_of': r.alias_of or None,
            'alias_kind': r.alias_kind or None,
            'file': r.file,
            'type': r.value_type,
            'default_status': r.default_status,
            'default_value': default_json_value(r),
            'category': r.category,
            'sample_observed': r.sample_observed,
            'source_defined': r.source_defined,
            'definition_source': r.definition_source,
            'observed_versions': list(r.observed_versions),
            'applicable_versions': list(r.applicable_versions),
            'approval': r.approval,
            'page': pages.get(r.key.lower()) if r.category == 'whitelist_candidate' else None,
        }
        if r.approval_note:
            entry['approval_note'] = r.approval_note
        if r.note:
            entry['note'] = r.note
        entries.append(entry)

    by_category = {slug: 0 for slug in CATEGORY_LABELS}
    by_approval = {slug: 0 for slug in APPROVALS}
    by_definition_source = {slug: 0 for slug in DEFINITION_SOURCES}
    by_alias_kind = {slug: 0 for slug in ALIAS_KINDS}
    observed_versions: dict[str, int] = {}
    for r in records:
        by_category[r.category] += 1
        by_approval[r.approval] += 1
        by_definition_source[r.definition_source] += 1
        if r.alias_kind:
            by_alias_kind[r.alias_kind] += 1
        if r.observed_versions:
            for version in r.observed_versions:
                observed_versions[version] = observed_versions.get(version, 0) + 1

    whitelist = [r for r in records if r.category == 'whitelist_candidate']
    with_page = sum(1 for r in whitelist if r.key.lower() in pages)
    whitelist_keys = sorted((r.key for r in whitelist), key=lambda k: (k.lower(), k))
    banned_total = sum(
        count for slug, count in by_category.items() if slug.startswith('banned_'))

    stats = {
        'total_keys': len(records),
        'whitelist_candidates': len(whitelist),
        'whitelist_approved': by_approval['approved'],
        'banned_total': banned_total,
        'banned_pending_review': by_approval['pending_review'],
        'source_defined_and_observed': sum(
            1 for r in records if r.sample_observed and r.source_defined),
        'observed_without_source_definition': sum(
            1 for r in records if r.sample_observed and not r.source_defined),
        'by_category': by_category,
        'by_approval': by_approval,
        'by_definition_source': by_definition_source,
        'by_alias_kind': by_alias_kind,
        'observed_versions': dict(sorted(observed_versions.items())),
        'pages': {
            'whitelist_with_page': with_page,
            'whitelist_without_page': len(whitelist) - with_page,
        },
    }

    return {
        'format_version': '1.0',
        'generated_by': 'tools/kb_index/build_field_dictionary.py',
        'source': 'tools/kb_index/field_dictionary.csv',
        'language': 'zh-CN',
        'status': 'draft',
        'scope': (
            'project_settings.config 的写入字段字典：白名单候选、六类禁入、'
            '别名与 schema 字段'
        ),
        'source_snapshot': SOURCE_SNAPSHOT,
        'sample_versions': list(SAMPLE_VERSIONS),
        'approval_policy': {
            'pending': '样本出现，批准写入与适用版本待维护者确认',
            'pending_review': '废弃候选，逐项定论待切片团队确认',
            'banned_draft': '草案六类禁入，随规范定稿确认',
            'approved': '维护者已确认可写入',
            'rejected': '维护者已拒绝写入',
        },
        'version_policy': (
            'applicable_versions 为空表示待维护者确认；'
            'observed_versions 仅表示样本中出现，不等同于适用版本'
        ),
        'references': REFERENCES,
        'category_labels': CATEGORY_LABELS,
        'stats': stats,
        'whitelist_candidate_keys': whitelist_keys,
        'keys': entries,
    }


def render(artifact: dict) -> str:
    return json.dumps(artifact, ensure_ascii=False, indent=2) + '\n'


def import_v0(v0_path: Path, metadata_path: Path) -> list[FieldRecord]:
    """Bootstrap the cleaned CSV from the internal v0 reconciliation."""
    if not v0_path.is_file():
        raise DictionaryError(
            f'v0 data not found: {v0_path} (--import-v0 is an internal bootstrap only)')
    if not metadata_path.is_file():
        raise DictionaryError(
            f'metadata JSON not found: {metadata_path} (--import-v0 is internal only)')

    try:
        with open(metadata_path, encoding='utf-8') as f:
            meta = json.load(f)['keys']
    except (json.JSONDecodeError, KeyError) as exc:
        raise DictionaryError(f'invalid metadata JSON {metadata_path}: {exc}') from exc
    meta_ci: dict[str, dict] = {}
    for key, value in meta.items():
        lower = key.lower()
        if lower in meta_ci:
            raise DictionaryError(f'metadata has case-insensitive duplicate: {key}')
        meta_ci[lower] = value

    with open(v0_path, encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        required = {'key', 'source_type', 'observed_in_samples', 'category'}
        if not required.issubset(reader.fieldnames or []):
            raise DictionaryError(
                f'v0 CSV is missing required columns: {sorted(required)}')
        v0_rows = list(reader)

    v0_keys = {row['key'].strip() for row in v0_rows}
    records: list[FieldRecord] = []
    for line, row in enumerate(v0_rows, start=2):
        key = (row.get('key') or '').strip()
        if not KEY_RE.fullmatch(key):
            raise DictionaryError(f'v0 line {line}: invalid key {key!r}')
        category = V0_CATEGORY_MAP.get((row.get('category') or '').strip())
        if category is None:
            raise DictionaryError(
                f'v0 line {line}: unknown category {(row.get("category") or "")!r}')
        observed_flag = (row.get('observed_in_samples') or '').strip()
        if observed_flag not in ('Y', '-'):
            raise DictionaryError(
                f'v0 line {line}: observed_in_samples must be Y/-, got {observed_flag!r}')
        sample_observed = observed_flag == 'Y'
        source_defined = bool((row.get('source_type') or '').strip())
        m = meta.get(key) or meta_ci.get(key.lower())

        alias_of = ''
        alias_kind = ''
        if key == 'project_schema_version':
            definition_source = 'runtime'
            alias_kind = 'schema_version'
        elif key.startswith('filament_') and m and m.get('derived'):
            base = key[len('filament_'):]
            if base not in v0_keys:
                raise DictionaryError(
                    f'v0 line {line}: derived base key {base!r} not in v0 CSV')
            definition_source = 'derived'
            alias_of = base
            alias_kind = 'legacy_prefix'
        elif not source_defined and key.startswith('machine_max_'):
            definition_source = 'macro'
            alias_kind = 'macro_declared'
        elif m and m.get('source') == 'hpp_macro':
            definition_source = 'macro'
        elif source_defined:
            definition_source = 'static'
        else:
            definition_source = 'unknown'

        value_type = logical_type(
            (m or {}).get('type') or (row.get('source_type') or '').strip())

        if m is None:
            default_status, default_value = 'unknown', ''
        else:
            default = m.get('default')
            if default is None:
                default_status, default_value = 'none', ''
            elif default == '':
                default_status, default_value = 'empty', ''
            else:
                default_status, default_value = 'static', str(default)

        if category == 'whitelist_candidate':
            approval = 'pending'
        elif category == 'banned_gui_deprecated':
            approval = 'pending_review'
        else:
            approval = 'banned_draft'

        if approval == 'pending':
            if key in ('printhost_authorization_type', 'printhost_ssl_ignore_revoke'):
                approval_note = '非凭据类主机连接设置；批准待定'
            elif key in ('inherits_group', 'different_settings_to_system'):
                approval_note = '规范 6.3 固定系统字段；批准待定'
            else:
                approval_note = '批准写入与适用版本待维护者确认'
        elif approval == 'pending_review':
            approval_note = '废弃候选，逐项定论待切片团队确认'
        elif category == 'banned_host_credentials':
            approval_note = '凭据类字段，安全禁入'
        else:
            approval_note = '草案六类禁入；随规范定稿确认'

        notes: list[str] = []
        if alias_kind == 'legacy_prefix':
            notes.append('遗留前缀别名；映射机制待确认')
        if alias_kind == 'macro_declared':
            if default_status == 'static':
                notes.append('头文件宏声明；配置定义由 PrintConfig.cpp 动态生成，默认值由源码提供')
            else:
                notes.append('头文件宏声明；默认值由预设提供')
        if key == 'required_nozzle_HRC':
            notes.append('落盘名保留大写 HRC；键页文件名为小写；v0/metadata 记为源码定义')
        if key == 'project_schema_version':
            notes.append('2.4.0 起落盘；缺失按 legacy 处理')
        if key in V204_FIELDS and key != 'project_schema_version':
            notes.append('2.4.0 样本新增；适用版本待确认')
        if key in ('inherits_group', 'different_settings_to_system'):
            notes.append('规范 6.3 固定系统字段（条件写入）')
        if key in ('printhost_authorization_type', 'printhost_ssl_ignore_revoke'):
            notes.append('非凭据类主机连接设置')
        if key == 'print_host_webui':
            notes.append('凭据类字段')

        records.append(FieldRecord(
            key=key,
            alias_of=alias_of,
            alias_kind=alias_kind,
            file='project_settings.config',
            value_type=value_type,
            default_status=default_status,
            default_value=default_value,
            category=category,
            category_label=CATEGORY_LABELS[category],
            sample_observed=sample_observed,
            source_defined=source_defined,
            definition_source=definition_source,
            observed_versions=('2.4.0',) if key in V204_FIELDS else (),
            applicable_versions=(),
            approval=approval,
            approval_note=approval_note,
            note='；'.join(notes),
        ))

    validate_records(records)
    return records


def summary(records: list[FieldRecord]) -> str:
    whitelist = sum(1 for r in records if r.category == 'whitelist_candidate')
    banned = sum(1 for r in records if r.category.startswith('banned_'))
    aliases = sum(1 for r in records if r.alias_kind == 'legacy_prefix')
    macros = sum(1 for r in records if r.alias_kind == 'macro_declared')
    schema = sum(1 for r in records if r.alias_kind == 'schema_version')
    return (
        f'{len(records)} keys | whitelist candidates {whitelist} | banned {banned} | '
        f'aliases {aliases} legacy + {macros} macro + {schema} schema'
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=SOURCE_CSV,
                        help='source CSV (default: tools/kb_index/field_dictionary.csv)')
    parser.add_argument('--out', type=Path, default=OUT_PATH,
                        help='output JSON (default: index/field_dictionary.json)')
    parser.add_argument('--check', action='store_true',
                        help='verify the committed JSON is up to date')
    parser.add_argument('--import-v0', action='store_true', dest='import_v0',
                        help='internal: rebuild the source CSV from docs/data v0')
    parser.add_argument('--v0', type=Path, default=V0_CSV,
                        help='internal v0 CSV (used with --import-v0)')
    parser.add_argument('--metadata', type=Path, default=METADATA_JSON,
                        help='internal metadata JSON (used with --import-v0)')
    args = parser.parse_args()

    if args.check and args.import_v0:
        print('[FAIL] --check and --import-v0 are mutually exclusive')
        return 1

    try:
        if args.import_v0:
            records = import_v0(args.v0, args.metadata)
            write_source(args.source, records)
            print(f'wrote {display_path(args.source)}')
            print(summary(records))
            return 0

        records = read_source(args.source)
        pages = load_pages()
        text = render(build_artifact(records, pages))

        if args.check:
            if not args.out.is_file():
                print(f'[FAIL] field dictionary missing: {args.out}')
                return 1
            current = args.out.read_text(encoding='utf-8')
            if current == text:
                print(f'field dictionary is up to date: {display_path(args.out)}')
                return 0
            diff = list(difflib.unified_diff(
                current.splitlines(), text.splitlines(),
                fromfile=display_path(args.out), tofile='regenerated', lineterm=''))
            print('\n'.join(diff[:60]))
            print('field dictionary is stale; run python tools/kb_index/build_field_dictionary.py')
            return 1

        args.out.parent.mkdir(parents=True, exist_ok=True)
        with open(args.out, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
        print(f'wrote {display_path(args.out)}')
        print(summary(records))
        return 0
    except DictionaryError as exc:
        print(f'[FAIL] {exc}')
        return 1
    except OSError as exc:
        print(f'[FAIL] I/O error: {exc}')
        return 1


if __name__ == '__main__':
    sys.exit(main())
