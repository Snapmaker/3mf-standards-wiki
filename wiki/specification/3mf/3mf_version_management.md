# 3MF 版本管理细则

← [Wiki 首页](../../home.md)

> 工程 `.3mf` 的五层版本标识、写入 / 读取约定与兼容规则。

## 目录

- [前言](#前言)
- [引言](#引言)
- [1 范围](#1-范围)
- [2 术语和定义](#2-术语和定义)
- [3 五层版本标识](#3-五层版本标识)
- [4 包内版本载体](#4-包内版本载体)
- [5 写入端约定](#5-写入端约定)
- [6 读取端行为](#6-读取端行为)
  - [6.1 双管线与同族判别](#61-双管线与同族判别)
  - [6.2 版本门现状](#62-版本门现状)
- [7 配置键兼容与失败语义](#7-配置键兼容与失败语义)
  - [7.1 反序列化链](#71-反序列化链)
  - [7.2 失败落点](#72-失败落点)
- [8 兼容性矩阵](#8-兼容性矩阵)
- [9 变更检查清单](#9-变更检查清单)
- [10 历史教训与已知问题](#10-历史教训与已知问题)
  - [10.1 历史教训](#101-历史教训)
  - [10.2 已知问题](#102-已知问题)
- [附录（资料性）深入阅读](#附录资料性深入阅读)

## 前言

本文讲解工程 `.3mf` 的版本标识、写入与读取约定，以及新旧版本互开时的兼容行为。五层版本标识与兼容性要求的规范级定义见 [3mf 工程文件规范](3mf_standard.md) 第 7 章；本文为该规范的配套说明文档，两者不一致时以规范为准。

本文基线为 Snapmaker Orca 2.4.x（2026-09），源码行号与提交号不在本文维护，具体以当前源码为准。

## 引言

工程 `.3mf` 同时携带五层互不相干的版本：文件格式版本、生成器版本、配置 schema 版本、子格式版本头与预设版本。正确区分这些版本，是判断文件能否被当前版本正确读取的前提。

本文先给出五层版本与包内载体，再说明写入 / 读取约定、配置键失败语义、兼容性矩阵与变更检查清单，最后汇总历史教训与已知问题。

本文第 1 章划定范围；第 2 章定义术语；第 3～4 章说明五层版本与包内载体；第 5～6 章说明写入端与读取端约定；第 7 章说明配置键兼容与失败语义；第 8～9 章给出兼容性矩阵与变更检查清单；第 10 章汇总历史教训与已知问题；深入阅读入口见文末附录。

## 1 范围

本文阐述工程 `.3mf` 的五层版本标识、包内各文件的版本载体、写入与读取约定，以及新旧版本互开时的兼容行为。

本文适用于需要读取 / 生成工程 `.3mf`、或评估格式变更兼容性的读者。

本文不涉及：包结构与各文件的业务字段（见 [project_settings.config：全局打印设置](project_settings_config.md)、[model_settings.config：对象与打印板信息](model_settings_config.md)）、完整字段字典（见 [3mf 工程文件规范](3mf_standard.md) 附录 D）。

## 2 术语和定义

| 术语 | 定义 |
|---|---|
| 版本层 | 工程包中独立演进的一套版本号；层与层之间不互相推断 |
| 文件格式版本 | `3dmodel.model` 的 `Snapmaker_Orca:3mfVersion` 元数据，标识子模型格式 |
| 生成器版本 | `Application` 元数据中的软件版本，用于同族判别与旧版迁移门槛 |
| schema 版本 | `project_settings.config` 内的 `project_schema_version`，标识配置键集的兼容世代 |
| 子格式版本头 | 条件性文本 / JSON 文件首行或字段中的版本号，供对应解析器分支 |
| 预设版本 | 内嵌预设 JSON 的 `version`，Semver 语义 |
| 同族文件 | `Application` 前缀为 `Snapmaker_Orca-` / `BambuStudio-` 的 3mf |
| legacy | 无版本头或旧命名空间的历史文件 / 键，按兼容规则解释 |

## 3 五层版本标识

| # | 版本层 | 载体 | 当前值 | 主要用途 |
|---|---|---|---|---|
| 1 | 文件格式版本 | `3dmodel.model` 内 `<metadata name="Snapmaker_Orca:3mfVersion">` | 1（兼容上限 2） | 子模型格式识别；超限检查已禁用 |
| 2 | 生成器（应用）版本 | `<metadata name="Application">Snapmaker_Orca-x.y.z` | 随构建 | 同族判别；旧版热床迁移门槛（<1.5.9） |
| 3 | 配置 schema 版本 | `project_settings.config` 内 `project_schema_version` | 1 | 新版文件升级提示（提示不拦截；递增规则待定） |
| 4 | 子格式版本头 | 各内嵌文件首行 / 字段 | 2 / 0 / 2 不等 | 对应解析器分支 |
| 5 | 预设版本 | 内嵌预设 JSON `version`；vendor profile `version` | Semver | 预设系统门控 |

五层互不相干，读取时不应互相推断。

## 4 包内版本载体

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

## 5 写入端约定

每次保存应：

1. 写 `Snapmaker_Orca:3mfVersion` = 1。该键不可停写：外拆子模型靠它识别格式，加密拆分对象回载依赖它。
2. 写 `Application` = `Snapmaker_Orca-<软件版本>`，不借用其他软件前缀，避免被当作同族工程。
3. 剥除 `BambuStudio:` / `bamboo_slicer:` 前缀的元数据键；读取端仍按三键等价兼容历史文件。
4. 隐私键（`DesignerUserId`、`CreationDate`、`ModificationDate`）恒置空。
5. `project_settings.config` 的 `version` 写软件版本，`project_schema_version` 写 1；内嵌预设写 Semver `version`。
6. 条件性文本文件带首行版本头；格式演进走版本头，不隐式变更。

## 6 读取端行为

### 6.1 双管线与同族判别

主管线负责本产品 3mf 的全部读写，并兼容读取同族文件；Prusa 管线只嗅探、只读 PrusaSlicer 3mf（只读几何，不加载配置）。判据：包内存在 `3D/_rels/3dmodel.model.rels` → 不是 Prusa；`Application` 含 `PrusaSlicer` → 是 Prusa。

同族判别只看 `Application` 前缀（`Snapmaker_Orca-` / `BambuStudio-`）；版本键命中不再置该标志。通用 Core 文件（`From_Other`）只加载几何并触发多实例拆分。

### 6.2 版本门现状

当前没有任何"版本过新即拒载"的硬门槛——格式版本超限、生成器主版本、未识别键弹窗等检查均已注释或禁用。仍在岗的只有三处：

- Prusa 文件只读几何；
- 生成器版本 `<1.5.9` 时做热床尺寸迁移；
- `project_schema_version` 高于自身支持时提示升级（提示，不拦截）。

## 7 配置键兼容与失败语义

### 7.1 反序列化链

先查 legacy 改名表，再按 `def` / `alias` 匹配键；未知键一律抛异常。替换规则只救"已知键的未知枚举 / 布尔值"，不救未知键。

### 7.2 失败落点

1. **主配置** `project_settings.config` 遇未知键：`load_from_json` 整体中止（后续键不再处理），但包仍能打开——几何与盘信息照常加载，本文件已解析键之后的内容（含预设标识 / 状态键）丢失，预设挂载回退默认，且无用户可见提示。
2. **内嵌预设** 遇未知键：静默跳过该预设。
3. **对象 / 零件级配置**（`model_settings.config` 内的裸键值）遇解析异常：无捕获穿透，**整个 3mf 导入中止**，文件打不开。

后果：新增配置键在旧版上要么静默丢配置，要么（对象 / 零件级）直接打不开新文件。发布窗口因此需要冻结新键；目标态是逐键容忍并记录未知键。

## 8 兼容性矩阵

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

## 9 变更检查清单

| 项 | 要点 |
|---|---|
| A 新增配置键 | 先登记字段字典；评估前向破坏（旧版丢配置或打不开）；读取路径不假设键存在 |
| B 修改键类型 | 标量↔向量双向检查；对象 / 零件级覆盖是暴露面；枚举只增不删，改名走 legacy 改名表 |
| C 改内嵌文件结构 | 新增文件安全（登记 Content_Types 与读取路由）；禁止删改既有文件名 / 元素名；平面文本加首行版本头 |
| D 动 schema | 仅"旧程序无法正确理解新文件"的不兼容变更才递增；提示不拦截，正确性靠读端迁移 |
| E 品牌 / 判别键 | 版本键不可停写；新增品牌同步扩展三键等价表与 `Application` 前缀判别 |
| F 发布前回归 | 新版开：自家旧版、同族软件各代、Prusa、MakerWorld 件、通用 Core；旧版开新版须有明确错误信息而非静默半载 |

## 10 历史教训与已知问题

### 10.1 历史教训

- 格式版本 v2 曾启用后回滚至 1；兼容上限仍为 2，下次不兼容变更应直接用 3。版本号一旦发布，回滚成本极高。
- 2026-09 高流量 coFloats 化：向量遇 `nil` 曾抛异常中止导入；现已改为跳过并告警。标量读双值只取前缀，向量灌标量有折叠兼容，反向不成立。
- 新增配置键会让旧版主配置静默丢配置——这是"新文件 → 旧程序"方向最实质的破坏面。
- 禁用版本门时，门内的语义迁移要迁到 schema / legacy 机制，不能一并埋掉。

### 10.2 已知问题

- `load_from_json` 遇未知键整体中止（目标：逐键容忍并记录）。
- 对象 / 零件级配置异常无捕获，会中止整个导入。
- 内嵌预设解到同一临时文件互相覆盖（上游遗留，多预设只剩最后一个）。
- CLI 纯 3mf 直切未按流量解析 2N 交错温度向量，可能切错温度。
- `plate` 元素无版本字段，盘结构演进没有版本抓手。

## 附录（资料性）深入阅读

- 规范级定义：[3mf 工程文件规范](3mf_standard.md) [§7 版本与兼容](3mf_standard.md#7-版本与兼容)、[§7.3 读取端行为](3mf_standard.md#73-读取端行为)、[§7.4 兼容性矩阵](3mf_standard.md#74-兼容性矩阵)。
- 文件字段说明：[project_settings.config：全局打印设置](project_settings_config.md)、[model_settings.config：对象与打印板信息](model_settings_config.md)。
