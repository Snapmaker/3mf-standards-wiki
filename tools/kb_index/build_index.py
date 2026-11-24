#!/usr/bin/env python3
"""Build index/kb_index.json for offline agent reading.

The index is a small, deterministic JSON file derived from Markdown only:

  * the 11 format-specification pages (3MF / gcode.3mf / preset), and
  * 12 representative setting key pages (pilot set).

It also points at the machine-readable field dictionary
(index/field_dictionary.json), built separately by
build_field_dictionary.py.

Curated metadata lives in two maintainer-edited files next to this script:
search_terms.json (Chinese search terms) and spec_meta.json (spec status,
version, scope, field-dictionary path and known gaps).

Usage:
  python tools/kb_index/build_index.py
  python tools/kb_index/build_index.py --check

--check rebuilds the index in memory and compares it with index/kb_index.json;
it exits 1 when the committed artefact is stale. No timestamps or commit
hashes are written, so repeated generation is byte-identical.
"""

import argparse
import difflib
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INDEX_PATH = ROOT / 'index' / 'kb_index.json'
GCODE_FIELDS = ROOT / 'wiki' / 'specification' / 'gcode.3mf' / 'gcode_3mf_interaction_fields.md'
OVERVIEWS = [
    ROOT / 'wiki' / 'settings' / 'printer' / 'printer_overview.md',
    ROOT / 'wiki' / 'settings' / 'filament' / 'filament_overview.md',
    ROOT / 'wiki' / 'settings' / 'process' / 'process_overview.md',
]

HEADING_RE = re.compile(r'^(#{2,3})\s+(.+)$')
META_RE = re.compile(r'^\[([^\]]+)\]\([^)]*\):\s*(.+)$')
LOCATION_RE = re.compile(r'^> Location:\s*(.+)$', re.M)
STATUS_RE = re.compile(r'^> Status:\s*(placeholder|cross-reference)', re.M)
GCODE_NAME_RE = re.compile(r'^> G-code embedded name:\s*`([^`]+)`', re.M)
OVERVIEW_RE = re.compile(r'^- (✅|🚧|🔗) \[`([^`]+)`\]\(([^)]+)\)(?:\s*\((.+)\))?')
LINK_RE = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')


def read(path):
    return path.read_text(encoding='utf-8')


def rel(path):
    return path.relative_to(ROOT).as_posix()


def normalize(text):
    text = text.lower()
    out = []
    for ch in text:
        cat = unicodedata.category(ch)
        if cat[0] in ('L', 'N', 'M'):
            out.append(ch)
        elif ch.isspace():
            out.append(' ')
    return re.sub(r' +', ' ', ''.join(out)).strip()


def github_slug(text):
    """Approximate GitHub's heading slug: keep letters/numbers/marks/_/-."""
    text = LINK_RE.sub(lambda m: m.group(1), text)
    text = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', text)
    text = text.replace('`', '').replace('*', '')
    text = re.sub(r'<[^>]+>', '', text)
    out = []
    for ch in text.strip().lower():
        cat = unicodedata.category(ch)
        if cat[0] in ('L', 'N', 'M') or cat == 'Pc' or ch == '-':
            out.append(ch)
        elif ch.isspace():
            out.append('-')
    return ''.join(out)


def parse_location(text):
    m = LOCATION_RE.search(text)
    if not m:
        return {}
    parts = [p.strip() for p in m.group(1).split('→')]
    out = {'tab': parts[0]} if parts else {}
    if len(parts) >= 2:
        out['group'] = parts[1]
    if len(parts) == 3:
        out['ui_label'] = parts[2]
    elif len(parts) >= 4:
        out['ui_block'] = parts[2]
        out['ui_label'] = parts[-1]
    return out


def parse_metadata(text):
    out = {}
    for line in text.splitlines():
        m = META_RE.match(line.strip())
        if not m:
            continue
        label, value = m.group(1).strip(), m.group(2).strip()
        if value.endswith('.'):
            value = value[:-1].rstrip()
        value = value.strip('`').strip()
        key = {
            'Mode': 'mode', 'Variable': 'variable', 'Type': 'type',
            'Default': 'default', 'Unit': 'unit', 'Range': 'range',
            'Aliases': 'aliases', 'Options': 'options',
            'CLI Example': 'cli_example',
        }.get(label)
        if key and value:
            out[key] = value
    return out


def parse_overviews():
    status, group = {}, {}
    group_is_cross = {}
    for ov in OVERVIEWS:
        for line in ov.read_text(encoding='utf-8').splitlines():
            m = OVERVIEW_RE.match(line.strip())
            if not m:
                continue
            marker, _key, target, label = m.groups()
            dest = (ov.parent / target).resolve()
            dest_rel = rel(dest)
            value = {'✅': 'complete', '🚧': 'placeholder', '🔗': 'cross_reference'}[marker]
            if dest_rel not in status or (status[dest_rel] == 'cross_reference' and value != 'cross_reference'):
                status[dest_rel] = value
            if label:
                # Keep the canonical group; do not let a cross-reference
                # occurrence overwrite a real overview entry.
                if dest_rel not in group or (group_is_cross.get(dest_rel) and value != 'cross_reference'):
                    group[dest_rel] = label
                    group_is_cross[dest_rel] = (value == 'cross_reference')
    return status, group


def parse_gcode_mappings():
    text = GCODE_FIELDS.read_text(encoding='utf-8')
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.startswith('### 3.3 '):
            start = i + 1
            break
    if start is None:
        return {}
    out = {}
    for line in lines[start:]:
        if line.startswith('### ') or line.startswith('## '):
            break
        m = re.match(r'^\|\s*`([^`]+)`\s*\|\s*\[([^\]]+)\]\(([^)]+)\)', line.strip())
        if not m:
            continue
        gcode_name, link_text, target = m.groups()
        if not link_text.isascii():
            continue
        dest = (GCODE_FIELDS.parent / target).resolve()
        out[rel(dest)] = gcode_name
    return out


def parse_outline(text):
    seen = {}
    outline = []
    in_fence = False
    for line in text.splitlines():
        if line.startswith('```'):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING_RE.match(line)
        if not m:
            continue
        level = len(m.group(1))
        title = m.group(2).strip()
        anchor = github_slug(title)
        if not anchor:
            continue
        count = seen.get(anchor, 0)
        seen[anchor] = count + 1
        if count:
            anchor = f'{anchor}-{count}'
        outline.append({'level': level, 'title': title.replace('`', ''), 'anchor': anchor})
    return outline


def setting_id(path):
    sub = path.relative_to(ROOT / 'wiki' / 'settings').with_suffix('')
    return 'setting.' + sub.as_posix().replace('/', '.')


def spec_id(path):
    if (ROOT / 'wiki' / 'specification') in path.parents:
        sub = path.relative_to(ROOT / 'wiki' / 'specification').with_suffix('')
        return 'spec.' + sub.as_posix().replace('/', '.')
    return 'spec.preset.' + path.stem


def build_setting_entry(path, status_by_path, group_by_path, gcode_map, search_terms):
    text = read(path)
    key = path.stem
    entry = {
        'id': setting_id(path),
        'kind': 'setting',
        'path': rel(path),
        'lang': 'en',
        'key': key,
    }
    entry.update(parse_location(text))
    meta = parse_metadata(text)
    entry.update(meta)
    if rel(path) in group_by_path:
        entry['overview_group'] = group_by_path[rel(path)]
    page_status = STATUS_RE.search(text)
    status = None
    if page_status:
        status = {'placeholder': 'placeholder', 'cross-reference': 'cross_reference'}[page_status.group(1)]
    status = status or status_by_path.get(rel(path)) or 'unknown'
    entry['status'] = status
    terms = search_terms.get(key) or search_terms.get(meta.get('variable', '').lower()) or []
    if terms:
        entry['search_terms'] = terms
    gcode_name = None
    m = GCODE_NAME_RE.search(text)
    if m:
        gcode_name = m.group(1)
    elif rel(path) in gcode_map:
        gcode_name = gcode_map[rel(path)]
    if gcode_name:
        entry['gcode_name'] = gcode_name
        entry['mapping_ref'] = rel(GCODE_FIELDS) + '#33-嵌入名字段'
    return entry


def build_spec_entry(path, meta):
    text = read(path)
    title = ''
    for line in text.splitlines():
        if line.startswith('# '):
            title = line[2:].strip()
            break
    kind = 'preset' if (ROOT / 'wiki' / 'preset') in path.parents else 'specification'
    entry = {
        'id': spec_id(path),
        'kind': kind,
        'path': rel(path),
        'lang': 'zh',
        'title': title,
        'family': meta['family'],
        'version': meta['version'],
        'status': meta['status'],
        'scope': meta['scope'],
        'outline': parse_outline(text),
    }
    return entry


def build_index():
    search_terms = json.loads(read(ROOT / 'tools' / 'kb_index' / 'search_terms.json'))
    spec_meta = json.loads(read(ROOT / 'tools' / 'kb_index' / 'spec_meta.json'))
    field_dictionary = spec_meta.get('field_dictionary')
    if field_dictionary and not (ROOT / field_dictionary).is_file():
        raise SystemExit('missing field dictionary: ' + field_dictionary)
    status_by_path, group_by_path = parse_overviews()
    gcode_map = parse_gcode_mappings()

    entries = []
    for path in sorted((ROOT / 'wiki' / 'settings').rglob('*.md')):
        if path.stem in search_terms:
            entries.append(build_setting_entry(path, status_by_path, group_by_path, gcode_map, search_terms))
    for path_str, meta in spec_meta['specs'].items():
        entries.append(build_spec_entry(ROOT / path_str, meta))

    for entry in entries:
        if not (ROOT / entry['path']).exists():
            raise SystemExit('missing indexed path: ' + entry['path'])
    entries.sort(key=lambda e: e['id'])

    return {
        'format_version': '0.1',
        'generated_by': 'tools/kb_index/build_index.py',
        'language': 'zh-CN',
        'entrypoint': 'wiki/home.md',
        'read_order': ['README.md', 'AGENTS.md', 'wiki/home.md'],
        'field_dictionary': field_dictionary,
        'known_gaps': spec_meta['known_gaps'],
        'entries': entries,
    }


def render(index):
    return json.dumps(index, ensure_ascii=False, indent=2) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='verify the committed index is up to date')
    args = parser.parse_args()

    text = render(build_index())
    if args.check:
        if not INDEX_PATH.exists():
            print('index missing:', INDEX_PATH)
            return 1
        current = INDEX_PATH.read_text(encoding='utf-8')
        if current == text:
            print('index is up to date:', rel(INDEX_PATH))
            return 0
        diff = list(difflib.unified_diff(
            current.splitlines(), text.splitlines(),
            fromfile=rel(INDEX_PATH), tofile='regenerated', lineterm=''))
        print('\n'.join(diff[:60]))
        print('index is stale; run python tools/kb_index/build_index.py')
        return 1

    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(INDEX_PATH, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    print('wrote', rel(INDEX_PATH), 'entries:', len(json.loads(text)['entries']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
