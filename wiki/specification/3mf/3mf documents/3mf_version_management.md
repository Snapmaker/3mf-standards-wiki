# Snapmaker Orca 3MF 版本管理细则

> 调研基线:main 分支(含 4a9bc310d "Build project 0917" / b626b4be6,2026-09-30 之后)。
> 所有行号以当时代码为准,重构后需复核。
> 关联文档:3MF颜色格式调研报告（文档待入库）、耗材-挤出机映射评审（文档待入库）。

---

## 1. 总览

### 1.1 双读写管线

| 管线 | 文件 | 职责 |
|---|---|---|
| **BBS 管线(主)** | `bbs_3mf.cpp` | 本产品 3mf 的**全部读写**;兼容读取 Bambu Studio 原生 3mf |
| **Prusa 管线(嗅探+只读)** | `3mf.cpp` | 仅识别并读取 PrusaSlicer 3mf(只读几何,不加载配置);本 fork 从不用它写文件 |

导入分发在 `Model.cpp:361-390`:
`.3mf` → `PrusaFileParser::check_3mf_from_prusa` 命中则走 `load_3mf` + `From_Prusa`;否则 `load_bbs_3mf`,按 `is_bbl_3mf` 出参细分 `From_BBS` / `From_Other`。

Prusa 判据(`3mf.cpp:288-341`):
① zip 内存在 `3D/_rels/3dmodel.model.rels` → **不是** Prusa(BBS 拆分模型才有);
② `3D/3dmodel.model` 的 Application 元数据含 `PrusaSlicer` → 是 Prusa。

### 1.2 五层版本标识总览

| # | 版本层 | 载体 | 当前值 | 主要消费方 |
|---|---|---|---|---|
| 1 | **文件格式版本** | `3D/3dmodel.model` 内 `<metadata name="Snapmaker_Orca:3mfVersion">` | 1(兼容上限 2) | sub-model 格式识别;超限检查已禁用 |
| 2 | **生成器(应用)版本** | `<metadata name="Application">Snapmaker_Orca-<Snapmaker_VERSION>` | 随构建 | `file_version`(Semver)出参;BBS 3mf 判别;1.5.9 热床迁移门槛 |
| 3 | **项目模式版本** | `Metadata/project_settings.config` 内 `project_schema_version`(int) | 1 | `handle_newer_3mf_schema` 升级提示 |
| 4 | **子格式版本头** | 各内嵌文件首行/字段(见 §2) | 2/0/2 不等 | 对应解析器的分支 |
| 5 | **预设版本** | 内嵌预设 JSON `version` 键;vendor profile `version` | Semver | `Preset.version`;PresetUpdater `min_version` 门控 |

另有 slice_info.config 的调试头 `X-SM-Client-Type/Version`(AA.BB.CC.DD 全宽格式,`bbs_3mf.cpp:7920-7923`,`Utils.hpp:116`)。

---

## 2. 3MF 包内结构与版本载体

### 2.1 内嵌文件清单

写入顺序由 `_BBS_3MF_Exporter::_add_required_file_to_archive` 编排(`bbs_3mf.cpp:5880-6290`)。路径常量集中 `bbs_3mf.cpp:149-196` 与 `bbs_3mf.hpp:22-31`。

| 文件 | 内容格式 | 携带的版本 |
|---|---|---|
| `[Content_Types].xml` | OPC 声明 | 无 |
| `_rels/.rels` | OPC 关系(model+缩略图) | 无 |
| `3D/3dmodel.model` | XML 几何+model 级元数据 | 格式版本、Application、MakerLabVersion |
| `Metadata/plate_N.png` 等 | 二进制缩略图(plate/no_light/top/pick/bbl_thumbnail) | 无 |
| `Metadata/plate_N.json` | 每盘首层 bbox JSON | **`version: 2`**(v1 颜色视图/v2 耗材 id 视图,`ThumbnailData.hpp:70-98`) |
| `Metadata/layer_heights_profile.txt` | 每对象层高剖面 | **首行 `layer_heights_profile_format_version=2`**(v1 隐式=对象序号,v2=3mf object id,写 `bbs_3mf.cpp:7317-7319`,读 `2769-2773`,常量 `184-185`) |
| `Metadata/layer_config_ranges.xml` | 变层高配置区间 | 无 |
| `Metadata/brim_ear_points.txt` | brim ear 点 | **首行 `brim_points_format_version=0`**(`hpp:144-146`) |
| `Metadata/custom_gcode_per_layer.xml` | 按层自定义 G-code | 无显式版本;靠 `<layer>` 缺 `type` 属性识别 PrusaSlicer ≤2.2.0 旧数据(`bbs_3mf.cpp:3182-3196`) |
| `Metadata/project_settings.config` | **JSON**(DynamicPrintConfig::save_to_json) | `version`=Snapmaker_VERSION(`bbs_3mf.cpp:7539`)+ **`project_schema_version`=1**(配置键本体) |
| `Metadata/{print,process,filament,machine}_settings_N.config` | 内嵌预设(旧 INI 已停用,现 JSON) | JSON `version`=预设 Semver(`bbs_3mf.cpp:7560`) |
| `Metadata/plate_N.gcode` + `.md5` | 每盘切片产物 | gcode 内嵌 CONFIG_BLOCK 随 config 全量键 |
| `Metadata/model_settings.config` | XML:对象/卷/盘(partplate)元数据 | 无自身版本;**对象/体积级 config 值裸写**(无前缀原名) |
| `Metadata/slice_info.config` | XML:每盘切片摘要 | 调试头 `X-SM-Client-Version` |
| `Metadata/cut_information.xml` | 切割/连接件信息 | 无 |
| `Auxiliaries/` | 附属文件 | 无 |

读取端按文件名路由的完整表:`bbs_3mf.cpp:1845-1936`。

### 2.2 model 级元数据键

写 `bbs_3mf.cpp:6608-6673`,读 `3816-3900`:
`Application`、`Title`、`Origin`、`Designer`/`DesignerUserId`(隐私置空)、`Description`、`Copyright`、`License`、`model_id`、`Region`、`CreationDate`/`ModificationDate`(隐私置空)、`MakerLab`/`MakerLabVersion`、版本键三胞胎。
无 "Producer" 键(那是通用 3MF core 概念,本管线不用)。

### 2.3 partplate(盘)结构

无独立 pickle/.idx 文件。plate 全部落在 `model_settings.config` 的 `<plate>` 元素 + `PlateData` 结构(`bbs_3mf.hpp:52-108`):`plater_id`(1 基)、`plater_name`、`locked`、`bed_type`、`print_sequence`、`spiral_mode`、`filament_map_mode`/`filament_maps`、`gcode_file`、各缩略图路径等。**plate 元素本身无版本字段**(`7721-7856` 键清单可证)。

---

## 3. 写入端细则

### 3.1 版本写入点(每次保存)

| 写什么 | 值 | 代码 |
|---|---|---|
| 格式版本键 | `Snapmaker_Orca:3mfVersion` = `VERSION_BBS_3MF`(=1) | `bbs_3mf.cpp:6650` |
| Application | `Snapmaker_Orca-<Snapmaker_VERSION>` | `bbs_3mf.cpp:6646` |
| project_settings.config `version` | Snapmaker_VERSION | `7539` |
| project_settings.config `project_schema_version` | `PROJECT_SCHEMA.current_version`(=1,配置键默认值自动携带) | `PrintConfig.cpp:4127-4134` |
| 内嵌预设 `version` | `preset->version.to_string()` | `7560` |
| slice_info 调试头 | `X-SM-Client-Version` = AA.BB.CC.DD | `7921-7922` |

### 3.2 去 Bambu 化策略(Snapmaker fork 刻意行为,来源 4a9bc310d)

1. **版本键改写自家命名空间**:保存只写 `Snapmaker_Orca:3mfVersion`;`BambuStudio:3mfVersion` / `bamboo_slicer:Version3mf` 降为**只读兼容别名**(读取三键等价,`bbs_3mf.cpp:3818-3820`)。
2. **Application 不再伪装 BambuStudio**:写 `Snapmaker_Orca-…`,注释明言"避免其他切片器把该 3mf 当成 Bambu 工程"(`6645-6646`)。
3. **剥除遗留 Bambu 品牌键**:从 metadata_items 删除所有 `BambuStudio:`/`bamboo_slicer:` 前缀键(`6616-6625`)。
4. **保留sub-model 识别钩子**:子模型文件仍写格式版本键,`ObjectImporter` 靠它识别 bbl 格式并恢复 uuid 后缀(`5422-5424` 读、`6648-6649` 注释)——**该键不可停写,否则加密拆分对象回载失败**。
5. 隐私:CreationDate/ModificationDate/DesignerUserId 恒置空(`6630`、`6642-6644`)。

### 3.3 SaveStrategy

保存策略位掩码(`bbs_3mf.hpp:111-130`):`WithGcode`(是否嵌 gcode)、`SplitModel`/`Encrypted`(加密拆分)、`Backup`(自动备份=WithGcode|Silence|SkipStatic|SplitModel)、`SkipModel`、`ShareMesh` 等。备份/恢复走 `Restore` LoadStrategy。

---

## 4. 读取端细则(决策流)

### 4.1 导入决策流(按序)

```
Plater::priv::load_files (Plater.cpp:11604)
 └─ Model::read_from_archive (Model.cpp:361)
     ├─ Prusa 嗅探命中 → load_3mf → En3mfType::From_Prusa
     │    └─ Plater.cpp:11894-11899:重置对象配置,只读几何+提示
     └─ load_bbs_3mf
          ├─ m_version ← 三键任一 (bbs_3mf.cpp:3818-3820;超限检查已注释 3821-3826)
          ├─ Application 前缀 "BambuStudio-"/"Snapmaker_Orca-"
          │    → m_is_bbl_3mf=true + 生成器 Semver (3827-3837)
          │    → file_version 出参 (1391-1393)
          ├─ m_version==0(无版本,第三方 3mf)
          │    → 多实例对象拆分等降级行为 (1942-1968)
          └─ En3mfType = From_BBS / From_Other (Model.cpp:388-390)
然后 Plater 侧:
 ① From_Prusa → 只读几何 (11894-11899)
 ② From_BBS && file_version < Semver(1,5,9) → translate_old 热床尺寸迁移 (12016-12020)
 ③ project_schema_version > 当前支持 → 弹"请升级"提示,继续加载 (handle_newer_3mf_schema, Plater.cpp:222-236, 调用点 11754)
 ④ unrecogized_keys 静默记录(config_substitutions, Plater.cpp:11732)
```

BBS 3mf 的判别**只看 Application 前缀**,版本键命中已不再置该标志(`3819` 注释)。`From_Other`(如通用 3MF core 文件)不加载配置、触发多实例拆分。

### 4.2 已禁用的版本检查清单(现状审计)

Orca 上游为互通性拆掉了 Bambu Studio 的硬版本门。**当前没有任何一道"版本过新即拒载"的硬门槛**,全部被注释或 `else if(false)`:

| 检查 | 位置 | 状态 |
|---|---|---|
| 格式版本 > 兼容上限(2)抛 version_error | `bbs_3mf.cpp:3821-3826` | 注释 |
| 生成器主版本 ≠ 应用主版本 → 不加载配置 | `bbs_3mf.cpp:1811-1822` "Orca: skip version check" | 注释 |
| 主版本不等 → 只读几何+重置对象配置 | `Plater.cpp:11900-11925` | 注释 |
| unrecognized_keys 弹"Newer 3mf version"窗 | `Plater.cpp:11950-11971` | `else if(false)` |
| 次版本不等提示升级 | `Plater.cpp:11974-11979` | `false` |
| sparse_infill_rotate_template 语义迁移 | `Plater.cpp:11927-11949` | `else if(false)` |
| 涂装数据版本检查(FDM/Seam/MM) | `bbs_3mf.cpp:3839-3850`,常量=0 `118-120` | 注释 |
| Newer3mfVersionDialog | `MsgDialog.cpp:517` | **从未实例化的死代码** |
| handle_legacy_project_loaded(brim 迁移) | `bbs_3mf.cpp:8585` | 调用被注释(Prusa 管线 3mf.cpp 仍启用) |

仍**在岗**的版本行为只有三处:Prusa 判别只读几何、`<1.5.9` 热床迁移、`project_schema_version` 升级提示(提示,不拦截)。

### 4.3 LoadStrategy

位掩码(`bbs_3mf.hpp:148-160`)。注意 `LoadConfig` 会自动附加 `CheckVersion`(`Plater.cpp:11719`),且 `m_check_version` 仍在赋值(`bbs_3mf.cpp:1343`)——但检查体已注释,该位目前**无效**,只具语义占位价值。

---

## 5. 配置键兼容规则(加载链)

### 5.1 反序列化链与失败语义

```
set_deserialize (Config.cpp:597)
 └─ set_deserialize_nothrow (579)
     ├─ handle_legacy:硬编码改名表/值改写 (PrintConfig.cpp:7609-7690)
     │    key 被清除 → 记 unrecogized_keys,return true 静默忽略
     └─ set_deserialize_raw (609)
          ├─ def 与 alias 均未命中 → throw UnknownOptionException (631) ← 无论 substitution rule
          └─ 值解析:
               枚举/布尔 → 按 rule 替换默认值并记 substitution (666-679)
               其他类型 → BadOptionValueException (599-600)
```

要点:
- **ForwardCompatibilitySubstitutionRule 只救"已知 key 的未知枚举值",不救未知 key**。未知 key 一律抛 `UnknownOptionException`。
- 对象/体积级配置(model_settings.config 里的裸键值)在对象装配时 `set_deserialize` 异常**无捕获穿透** → 整个 3mf 导入中止(见 §7 案例 1)。

### 5.2 project_settings.config / 内嵌预设的 JSON 加载

- `load_from_json` 遇未知 key 抛异常后,被函数尾部兜底 `catch(std::exception&)` 捕获 → **return -1,整个文件中止,后续键不再处理**(`Config.cpp:897/995/1102-1105`)。
- 落点:
  - 主配置失败 → `add_error` → **3mf 导入失败**(`bbs_3mf.cpp:2585-2589`)——"旧版程序打不开新版保存的 3mf"的直接机制;
  - 内嵌预设失败 → 静默跳过该预设(`2617-2622`);
  - 用户预设目录加载失败 → **删除该预设 .json/.info 文件**(`Preset.cpp:1291-1304`);version 键缺失/非法 → 跳过(`1328-1331`)。
- 数组灌标量的兼容:全等数组折叠为单值(`Config.cpp:960-973`)。
- coFloats 向量 deserialize 按逗号逐项解析、恒 return true;**"nil" 项:nullable 向量存 nil 值,非 nullable 向量跳过+warning**(`Config.hpp:657-686`,4a9bc310d 修复,此前 throw ConfigurationError)。
- 跨键复合迁移 `handle_legacy_composite`(整份 config 装载后,`PrintConfig.cpp:7776-7825`)——高流量双值键的 1→2 补齐挂这里。
- **容忍范本**:`load_string_map` 对每个 key 单独 try/catch 后 continue(`Config.cpp:794-800`)——若要修"未知 key 中止",照此改 load_from_json。

### 5.3 预设/供应商版本

- 内嵌预设 `version` → `Preset.version`(Semver),缺失时回退生成器版本(`bbs_3mf.cpp:2667-2673`)。
- vendor profile 根 JSON `version` 解析失败抛错(`PresetBundle.cpp:3257-3263`)。
- 系统预设升级门控:缓存 JSON 的 `min_version` > 当前 Snapmaker_VERSION → 标记 illegal 不自动安装(`PresetUpdater.cpp:1783-1806`)。
- 预设改名追踪:`renamed_from`(`Preset.hpp:70`,`Config.cpp:889-890`)。
- 预设兼容性表达**只有** `compatible_printers/compatible_prints(+condition)`,无 compatible_version 字段(`Preset.cpp:716-780`)。

---

## 6. 兼容性矩阵(实际生效行为)

| 场景 | 行为 | 机制 |
|---|---|---|
| 旧版文件 → 新程序 | ✅ 尽力迁移 | 无版本=0;handle_legacy 改名;handle_legacy_composite 补齐;数组折叠 |
| 新版文件 → 旧程序(未知新键) | ❌ **打不开** | load_from_json 未知 key 中止(§5.2);**无提示、无降级** |
| 新版文件 → 旧程序(已知键多值/类型变化) | ⚠️ 取决于反序列化 | 标量读双值只取前缀(静默丢尾);向量遇 nil(≤2.3.6)抛异常中止 |
| schema 升版文件 → 旧程序 | ⚠️ 弹提示继续加载 | handle_newer_3mf_schema(**仅对已带 project_schema_version 且读端有此逻辑的版本生效**;已发布 ≤2.3.x 无此代码,无法补救) |
| Bambu Studio 3mf → 本程序 | ✅ 完整加载 | Application 前缀判别;nil 已容忍(§7 案例 1 修复后) |
| 本程序 3mf → Bambu Studio | ✅ 按非 BBS 项目处理 | Application 不再写 BambuStudio-;Bambu 读端走通用兼容路径 |
| PrusaSlicer 3mf → 本程序 | ✅ 仅几何 | From_Prusa 分支重置配置 |
| 通用 3MF core → 本程序 | ✅ 仅几何 | From_Other;多实例拆分 |
| 本程序 → PrusaSlicer | ✅ 通用 core 几何可读 | 标准 core schema(`3dmodel.model xmlns`) |

---

## 7. 历史案例复盘

### 案例 1:coFloats 化 × Bambu 2.6 双热端工程打不开(2026-09,已修复)

- **变更**:784cfd18b(高流量合把,#794)把速度/加速度等几十键 coFloat→coFloats(双值:0=标准,1=高流量)。
- **触发**:MakerWorld 上 BambuStudio-02.06 保存的 3mf(双直驱热端预设)含 `"bridge_speed": ["30","nil"]`(嵌入预设 JSON)与 `value="30,nil"`(model_settings.config 对象级,实测一案 220 处/11 键)。"nil"=该热端无高流量变体。
- **两层失败**:嵌入预设层被 load_from_json 捕获→跳过(非致命);**致命层**=对象装配 `set_deserialize("bridge_speed","30,nil")` 抛 `ConfigurationError` 穿透 → 导入中止、弹错、无盘创建。
- **行为差异根因**:2.3.6 标量 coFloat 的 `istringstream >> value` 对 "30,nil" 只取前导 30 静默忽略;2.4.0 向量逐项解析遇 nil 抛异常。
- **修复**:4a9bc310d(2026-09-30)——非 nullable 向量 nil 项改为跳过+warning(`Config.hpp:670-677`)。同一提交引入 SNAPMAKER_3MF_VERSION 新键。
- **教训**:①键类型从标量放宽为向量≠无害——反向(向量灌标量读端)有折叠兼容,正向(旧数据灌新向量)逐项严格;②对象/体积级 config 反序列化异常会中止整个导入,是 3mf 兼容事故的最大暴露面;③跨厂商文件(MakerWorld 分发)必须进回归矩阵。

### 案例 2:新增配置键 → 旧版打不开新 3mf(结构性风险,未修)

- 机制见 §5.2:load_from_json 未知 key 抛异常,兜底 catch return -1,主配置失败即导入失败。
- 评审出处:耗材-挤出机映射评审（文档待入库） P0(2026-10-14):新增 `load_from_json` 不容忍的键时,旧版读端整包拒载。
- 这是"新文件→旧程序"方向上**唯一真正的拦截器**,也是发布窗口必须冻结新键的原因。

### 案例 3:格式版本 v2 回滚史(上游遗产)

`bbs_3mf.cpp:103-108`:v2(体积矩阵入 model config)曾启用后回滚到 1,注释警告**下次变更必须用 3**。当前兼容上限仍写 2(读得进 v2 文件),写入恒 1。教训:文件格式版本号一旦发布,回滚成本极高;动它需全生态协调。

### 案例 4:版本门禁用 → 语义迁移一并丢失

sparse_infill_rotate_template 的"2.2.0-alpha 工程非安全填充图案清洗"逻辑挂在版本门内,门被 `else if(false)` 后该迁移永久失效(`Plater.cpp:11927-11949`)。教训:禁用版本门时,门内的**语义迁移**要迁移到 schema/legacy 机制,不能一并埋掉。

---

## 8. 变更检查清单(细则落点)

改动 3mf 相关代码时逐项核对:

**A. 新增配置键**
1. 在 `PrintConfig.cpp` `init_print_config_def/...` 注册——注册后自动进 project_settings.config、内嵌预设、gcode CONFIG_BLOCK,无需单独写序列化。
2. 评估前向破坏:新键会让**所有已发布旧版**拒载新 3mf(§5.2)。若必须加:集中在一个发布窗口、提前公告,并考虑同步在 load_from_json 落地"逐 key 容忍"后再放量。
3. 向后兼容:旧文件无此键 → 靠 def 默认值或 handle_legacy_composite 补齐,**禁止在读取路径假设键存在**。

**B. 修改键类型**
1. 标量→向量:检查旧值反序列化(单值灌向量 OK);**检查所有裸 set_deserialize 调用点**(对象/体积级 config 是暴露面)。
2. 向量→标量:数值截断风险(取前缀),需可接受。
3. 枚举增删:枚举值删除会让旧文件值解析失败(有 substitution 兜底仅限枚举/布尔);**只增不删,重命名走 handle_legacy 改名表**(`PrintConfig.cpp:7609-7690`)。

**C. 改内嵌文件结构**
1. 新增文件:安全(旧版按未知文件忽略);需在 [Content_Types] 与读取路由表(`bbs_3mf.cpp:1845-1936`)登记。
2. 删除/改名既有文件、改元素名:破坏旧版读新文件——禁止,或给新文件名。
3. 平面文本格式演进:学 layer_heights_profile 加**首行版本头**(v1 隐式缺省=旧格式),解析器按头分支。

**D. 动 schema(project_schema_version)**
1. 何时 bump:发生了"旧程序无法正确理解新文件"的**不兼容**变更(而不仅是新增),且新版读端能为旧 schema 值做迁移。
2. bump 后旧程序(≥引入该机制的版本)会弹"请升级"提示但**继续加载**——提示不是拦截,数据正确性仍靠读端迁移代码保证。
3. 已发布且无此机制的版本(≤2.3.x)对任何 schema 值都无感知——schema 不能替代键级兼容。

**E. 品牌/判别键**
1. `Snapmaker_Orca:3mfVersion` 不可停写(sub-model 识别依赖,`6648-6649`)。
2. 读端三键等价表(`3818`)新增品牌时同步扩展。
3. Application 前缀判别(`3830-3836`)改品牌时,注意 substr 偏移=前缀长度("Snapmaker_Orca-"=15)。

**F. 发布前回归矩阵**
1. 新版开:自家旧版各代 3mf、Bambu Studio 各代(2.6+ 重点)、PrusaSlicer 导出、MakerWorld 下载件、通用 core 3MF。
2. 旧版开新版 3mf:确认预期行为(拒载/降级/提示)且**有错误信息而非静默半载**。
3. 加密/拆分对象(SplitModel)回载。
4. CLI 纯 3mf 直切路径(已知 2N 交错向量缺口,§9)。

---

## 9. 遗留问题与改进建议

| # | 问题 | 影响 | 建议 |
|---|---|---|---|
| 1 | load_from_json 未知 key 整体中止 | 新键发布=旧版拒载,发布窗口被迫冻结键(案例 2) | 照 load_string_map 范本改逐 key try/catch,未知键入 unrecogized_keys;主配置路径优先 |
| 2 | 对象/体积级 config 异常穿透中止导入 | 任何键值解析回归都是"打不开文件"级事故(案例 1 模式) | 装配路径按对象捕获降级(丢该键/该对象配置,保几何) |
| 3 | `_extract_project_embedded_presets` 全部解到同一 `_temp_2.config` 互相覆盖(上游遗留) | 多内嵌预设只剩最后一个 | 逐文件独立临时名 |
| 4 | `filament_map`/`filament_map_mode` 只写不读、未注册 | 写入死数据;unrecogized 噪声 | 注册或停写 |
| 5 | Newer3mfVersionDialog 死代码 + 5 处注释门 | "新 3mf→旧版提示"需求(高流量 wiki 9.8②)在**旧版侧**无解;代码语义误导后来者 | 要么恢复启用,要么删除并在此文档登记 |
| 6 | CLI 纯 3mf 直切:2N 交错温度向量未按流量解析(单耗材丢 HF 选择/多挤出机跨槽位取错值) | 云端/CI 若用 CLI 直切 GUI 工程会切错温 | CLI 路径复用 GUI 合并逻辑 |
| 7 | 生成器版本兜底 `Semver("0.0.0.0")` 与 dont_load_config 被注释 | 非 BBS Application 的文件也全量加载配置 | 确认是否刻意;若恢复注意 Third-party 文件行为 |
| 8 | `LoadStrategy::CheckVersion` 位仍在传递但检查体已注释 | 语义占位,易误读 | 保留占位可在本细则登记,或清理 |
| 9 | plate 元素无版本字段 | plate 结构演进无版本抓手 | 下次 plate 结构不兼容变更时,考虑 plate 级 `version` 属性或复用 schema 版本 |

---

## 10. 代码索引

| 主题 | 文件:行 |
|---|---|
| 格式版本常量与历史注释 | `bbs_3mf.cpp:103-124` |
| 版本键解析(读) | `bbs_3mf.cpp:3816-3850` |
| Application 判别+Semver | `bbs_3mf.cpp:3827-3837` |
| sub-model 版本键识别 | `bbs_3mf.cpp:5420-5426` |
| 元数据写入(含去Bambu化) | `bbs_3mf.cpp:6608-6673` |
| ProjectSchemaRegistry | `ProjectSchemaVersion.cpp` 全文 / 注册 `PrintConfig.cpp:4127-4134` |
| schema 提示 | `Plater.cpp:222-236` |
| 导入主流程 | `Plater.cpp:11604-12200` |
| 分发 | `Model.cpp:361-390` |
| Load/SaveStrategy | `bbs_3mf.hpp:111-172` |
| set_deserialize 链 | `Config.cpp:579-679` |
| load_from_json 中止路径 | `Config.cpp:832-1105` |
| coFloats nil 容忍 | `Config.hpp:657-686` |
| handle_legacy 改名表 | `PrintConfig.cpp:7609-7690` |
| handle_legacy_composite | `PrintConfig.cpp:7776-7825` |
| 预设版本/删除策略 | `Preset.cpp:1291-1331` |
| Prusa 嗅探 | `3mf.cpp:288-341` |
| 版本键引入提交 | 4a9bc310d(2026-09-30,SNAPMAKER_3MF_VERSION+nil 容忍);87f34b9a6(2026-09-01,project_schema_version);784cfd18b(2026-09-01,coFloats 化,案例 1 源头) |
