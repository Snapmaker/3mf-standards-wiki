# Snapmaker Orca 3MF 版本管理细则

← [Wiki 首页](../../home.md)

> 实现说明：基线 Snapmaker Orca 2.4.x（2026-09）。源码行号与提交号不在本文维护，具体以当前源码为准。

## 目录

- [1 五层版本标识](#1-五层版本标识)
- [2 包内版本载体](#2-包内版本载体)
- [3 写入端约定](#3-写入端约定)
- [4 读取端行为](#4-读取端行为)
- [5 配置键兼容与失败语义](#5-配置键兼容与失败语义)
- [6 兼容性矩阵](#6-兼容性矩阵)
- [7 变更检查清单](#7-变更检查清单)
- [8 历史教训与已知问题](#8-历史教训与已知问题)

## 1 五层版本标识

| # | 版本层 | 载体 | 当前值 | 主要用途 |
|---|---|---|---|---|
| 1 | 文件格式版本 | `3dmodel.model` 内 `<metadata name="Snapmaker_Orca:3mfVersion">` | 1（兼容上限 2） | 子模型格式识别；超限检查已禁用 |
| 2 | 生成器（应用）版本 | `<metadata name="Application">Snapmaker_Orca-x.y.z` | 随构建 | 同族判别；旧版热床迁移门槛（<1.5.9） |
| 3 | 配置 schema 版本 | `project_settings.config` 内 `project_schema_version` | 1 | 新版文件升级提示（提示不拦截；递增规则待定） |
| 4 | 子格式版本头 | 各内嵌文件首行 / 字段 | 2 / 0 / 2 不等 | 对应解析器分支 |
| 5 | 预设版本 | 内嵌预设 JSON `version`；vendor profile `version` | Semver | 预设系统门控 |

五层互不相干，读取时不应互相推断。

## 2 包内版本载体

| 文件 | 版本载体 |
|---|---|
| `3D/3dmodel.model` | `Snapmaker_Orca:3mfVersion`（格式版本）+ `Application`（生成器版本） |
| `Metadata/project_settings.config` | `version`（软件版本）+ `project_schema_version`（schema 版本） |
| `Metadata/*_settings_N.config` | JSON `version`（预设 Semver） |
| `Metadata/plate_N.json` | `version: 2` |
| `Metadata/layer_heights_profile.txt` | 首行 `layer_heights_profile_format_version=2` |
| `Metadata/brim_ear_points.txt` | 首行 `brim_points_format_version=0` |
| `Metadata/slice_info.config` | 调试头 `X-SM-Client-Version`（AA.BB.CC.DD，仅诊断） |
| `Metadata/model_settings.config` | 无版本字段（对象 / 零件 / 盘均无） |

`plate_N.json` 的 `version:2` 与 `layer_heights_profile` 的 v2 按首行 / 字段版本分支解析；无版本头的旧文件按 legacy 规则解释。

## 3 写入端约定

每次保存应：

1. 写 `Snapmaker_Orca:3mfVersion` = 1。该键不可停写：外拆子模型靠它识别格式，加密拆分对象回载依赖它。
2. 写 `Application` = `Snapmaker_Orca-<软件版本>`，不借用其他软件前缀，避免被当作同族工程。
3. 剥除 `BambuStudio:` / `bamboo_slicer:` 前缀的元数据键；读取端仍按三键等价兼容历史文件。
4. 隐私键（`DesignerUserId`、`CreationDate`、`ModificationDate`）恒置空。
5. `project_settings.config` 的 `version` 写软件版本，`project_schema_version` 写 1；内嵌预设写 Semver `version`。
6. 条件性文本文件带首行版本头；格式演进走版本头，不隐式变更。

## 4 读取端行为

**双管线**：主管线负责本产品 3mf 的全部读写，并兼容读取同族文件；Prusa 管线只嗅探、只读 PrusaSlicer 3mf（只读几何，不加载配置）。判据：包内存在 `3D/_rels/3dmodel.model.rels` → 不是 Prusa；`Application` 含 `PrusaSlicer` → 是 Prusa。

**同族判别**：只看 `Application` 前缀（`Snapmaker_Orca-` / `BambuStudio-`）；版本键命中不再置该标志。通用 Core 文件（`From_Other`）只加载几何并触发多实例拆分。

**版本门现状**：当前没有任何"版本过新即拒载"的硬门槛——格式版本超限、生成器主版本、未识别键弹窗等检查均已注释或禁用。仍在岗的只有三处：

- Prusa 文件只读几何；
- 生成器版本 `<1.5.9` 时做热床尺寸迁移；
- `project_schema_version` 高于自身支持时提示升级（提示，不拦截）。

## 5 配置键兼容与失败语义

反序列化链：先查 legacy 改名表，再按 `def` / `alias` 匹配键；未知键一律抛异常，替换规则只救"已知键的未知枚举 / 布尔值"，不救未知键。

失败语义分三级：

1. **主配置** `project_settings.config` 遇未知键：`load_from_json` 整体中止（后续键不再处理），但包仍能打开——几何与盘信息照常加载，本文件已解析键之后的内容（含预设标识 / 状态键）丢失，预设挂载回退默认，且无用户可见提示。
2. **内嵌预设** 遇未知键：静默跳过该预设。
3. **对象 / 零件级配置**（`model_settings.config` 内的裸键值）遇解析异常：无捕获穿透，**整个 3mf 导入中止**，文件打不开。

后果：新增配置键在旧版上要么静默丢配置，要么（对象 / 零件级）直接打不开新文件。发布窗口因此需要冻结新键；目标态是逐键容忍并记录未知键。

## 6 兼容性矩阵

| 场景 | 行为 | 机制 |
|---|---|---|
| 旧版文件 → 新程序 | ✅ 尽力迁移 | 无版本视为 0；legacy 改名表；数组折叠 |
| 新版文件 → 旧程序（未知新键，主配置） | ⚠️ 配置静默丢失 | `load_from_json` 中止，包仍可打开 |
| 新版文件 → 旧程序（未知新键，对象 / 零件级） | ❌ 打不开 | 反序列化异常穿透，导入中止 |
| 新版文件 → 旧程序（已知键值变化） | ⚠️ 取决于反序列化 | 标量读双值取前缀（静默丢尾）；旧版向量遇 `nil` 可能异常 |
| schema 升版 → 旧程序（≥2.4.0） | ⚠️ 提示后继续 | `handle_newer_3mf_schema`；≤2.3.x 无感知 |
| Bambu Studio 3mf → 本程序 | ✅ 完整加载 | `Application` 前缀判别；`nil` 已容忍 |
| 本程序 3mf → Bambu Studio | ✅ 按外来项目处理 | `Application` 不再写 `BambuStudio-` |
| PrusaSlicer 3mf → 本程序 | ✅ 仅几何 | Prusa 分支重置配置 |
| 通用 3MF Core → 本程序 | ✅ 仅几何 | `From_Other`；多实例拆分 |
| 本程序 → PrusaSlicer / 通用查看器 | ✅ 几何可读 | Core 兼容几何层 |

## 7 变更检查清单

| 项 | 要点 |
|---|---|
| A 新增配置键 | 先登记字段字典；评估前向破坏（旧版丢配置或打不开）；读取路径不假设键存在 |
| B 修改键类型 | 标量↔向量双向检查；对象 / 零件级覆盖是暴露面；枚举只增不删，改名走 legacy 改名表 |
| C 改内嵌文件结构 | 新增文件安全（登记 Content_Types 与读取路由）；禁止删改既有文件名 / 元素名；平面文本加首行版本头 |
| D 动 schema | 仅"旧程序无法正确理解新文件"的不兼容变更才递增；提示不拦截，正确性靠读端迁移 |
| E 品牌 / 判别键 | 版本键不可停写；新增品牌同步扩展三键等价表与 `Application` 前缀判别 |
| F 发布前回归 | 新版开：自家旧版、同族软件各代、Prusa、MakerWorld 件、通用 Core；旧版开新版须有明确错误信息而非静默半载 |

## 8 历史教训与已知问题

**历史教训**

- 格式版本 v2 曾启用后回滚至 1；兼容上限仍为 2，下次不兼容变更应直接用 3。版本号一旦发布，回滚成本极高。
- 2026-09 高流量 coFloats 化：向量遇 `nil` 曾抛异常中止导入；现已改为跳过并告警。标量读双值只取前缀，向量灌标量有折叠兼容，反向不成立。
- 新增配置键会让旧版主配置静默丢配置——这是"新文件 → 旧程序"方向最实质的破坏面。
- 禁用版本门时，门内的语义迁移要迁到 schema / legacy 机制，不能一并埋掉。

**已知问题**

- `load_from_json` 遇未知键整体中止（目标：逐键容忍并记录）。
- 对象 / 零件级配置异常无捕获，会中止整个导入。
- 内嵌预设解到同一临时文件互相覆盖（上游遗留，多预设只剩最后一个）。
- CLI 纯 3mf 直切未按流量解析 2N 交错温度向量，可能切错温度。
- `plate` 元素无版本字段，盘结构演进没有版本抓手。
