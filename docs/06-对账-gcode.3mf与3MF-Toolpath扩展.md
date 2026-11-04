# 对账：gcode.3mf × 3MF Toolpath Extension —— 切片结果交换的两条路线

> 目的：把本仓库 gcode.3mf 规范（v0.9.9）与 3MF 联盟 Toolpath Extension（1.0.0 RC）逐机制对账，为 gcode.3mf 专题提供行业背景与标准化动向的证据链。
> 日期：2026-11-04　状态：初稿（基于两份规范文本对账，未做互转实验）
> 证据来源：
> - 《3MF Toolpath Extension》Spec & Reference Guide **1.0.0 Release Candidate**（联盟发布，修订史 2026-09-03）——本地 `Downloads/3MF Toolpath Extension.md`，全文 1765 行精读
> - 《gcode.3mf 规范 v0.9.9 版》（实测样本 Seat_PLA_1h52m.gcode.3mf；技术内容已并入本仓库 `wiki/specification/gcode.3mf/gcode_3mf_standard.md` v1.0 草案）
> - 《3MF Core Specification》1.4.0 §2.2（命名约定核对）
> 关联：docs/04 问题清单（Q1–Q22）。

## 0. 结论速览

1. **不是竞争替代关系，是两种哲学**：Toolpath 扩展交换的是"可装载校验、机器端再编译"的结构化中间表示；gcode.3mf 交换的是"直接执行的最终代码"。同一托盘打印任务，两者给出的是不同深度的产物。
2. **技术重心不同**：Toolpath RC 以 LPBF（激光粉末床）为第一公民——多激光扫描场、跨激光同步、功率调制是它的核心卖点；FFF/deposition 只有 3 个标准参数（depositionspeed/beadwidth/beadheight），温度/风扇/回抽等消费级 FFF 必备参数没有标准槽位。
3. **短期无兼容压力**：RC 状态（2026-09 才首发）、零消费级落地、硬依赖 Production 扩展。对 fork 而言是观察项，不是行动项。
4. **两边的校验哲学值得互相借鉴**：Toolpath 的"装载期即可断言包络"（modifier 归一化）与 gcode.3mf 的"执行前字节校验"（MD5 + 四方交叉验证）解决的是不同层面的问题，不冲突。

## 1. 对账对象身份

| 项 | 3MF Toolpath Extension | gcode.3mf |
|---|---|---|
| 版本/状态 | 1.0.0 **Release Candidate**（2026-09-03 首发） | v0.9.9（内部规范，已量产使用） |
| 发布方 | 3MF 联盟（标准化轨道） | Snapmaker Orca fork（BBS 约定族） |
| 依赖 | Core 1.x + **Production 1.x（双 MUST**，RC Preface/Ch.1） | 无联盟扩展依赖（仅用 OPC 骨架 + 自有 Metadata 约定） |
| 命名空间 | `http://schemas.3mf.io/3dmanufacturing/toolpath/2026/03`（前缀 tp） | BBS 约定：`schemas.bambulab.com/package/2021`（历史）/ `schemas.snapmaker.com/package/2026`（新） |
| 推荐文件名 | `.build.3mf`（informative，RC Ch.3） | `.gcode.3mf`（双扩展，恰合 Core 1.4.0 §2.2.1 厂商约定 `.vendor.3mf` 的模式） |

Production 硬依赖的原因：RC 全链路用 UUID 引用（toolpathresource / profile / build item），而 Core 自身不提供稳定 UUID——这正是 Production 扩展的职责（RC §1、Glossary）。

## 2. 设计哲学对照

| | Toolpath RC | gcode.3mf v0.9.9 |
|---|---|---|
| 交换物 | 运动+曝光**数据**，机器端编译成指令 | 已切片完成的 **G-code 文本**，所见即所得 |
| 给谁读 | 机器控制栈（编译器/调度器） | 固件 G-code 解释器（直接执行） |
| 信任模型 | 消费者装载时校验能力与包络，**不能执行就整包拒绝** | 容器解析通过 ≠ 可执行；能力由机型预设/G-code 方言决定（v0.9.9 §5.4） |
| 数据组织 | 索引（模型文档）与数据（每层独立 part）分离，支持随机访问/流式 | 盘索引（model_settings.config）与数据（整板单文件 gcode）分离，但 gcode 本身不可随机访问 |

## 3. 包结构对照

**Toolpath RC**（RC Ch.3–4）：

```text
xxx.build.3mf
├── [Content_Types].xml / _rels/.rels          ← OPC 骨架（Core 规则）
├── /3D/3dmodel.model                           ← 含 <tp:toolpathresource>（索引）
│     lasersources + toolpathprofiles + toolpathlayers + toolpathdata
│     <build tp:toolpathid="1">                 ← 选哪套 toolpath
└── /Toolpath/Layers/layerNNNNN.xml             ← 每层一个 part（几何+层内局部表）
      通过 OPC 关系 …/toolpath/2026/03/layer 绑定
```

**gcode.3mf**（v0.9.9 §0）：

```text
xxx.gcode.3mf
├── [Content_Types].xml / _rels/.rels           ← OPC 骨架
├── /3D/3dmodel.model                           ← 元数据壳（SkipModel：无几何、无扩展资源）
├── /Auxiliaries/                               ← 封面缩略图等
└── /Metadata/                                  ← 全部核心内容
      model_settings.config（盘索引）→ plate_N.gcode（★整板文本）+ .md5
      + slice_info / plate_N.json / 缩略图族 / 配置快照 / 内嵌预设
```

结构性差异一句话：Toolpath 把"一托盘"切成"每层一个文件"，gcode.3mf 把"一托盘"保持为"每盘一个文件"。

## 4. 机制逐项对账

| # | 维度 | 3MF Toolpath RC（§引用） | gcode.3mf v0.9.9（§引用） |
|---|---|---|---|
| 1 | 坐标与单位 | **整数设备单位** × `unitfactor` = 文档单位（建议 mm）；定点表示，尺寸可控（RC Part II 开篇、§4 toolpathresource） | G-code 文本浮点 mm；精度由文本表示决定（§5.4） |
| 2 | 几何原语 | loop / polyline / hatch（平面）+ polyline3d / polyline6d（点带 z、四元数姿态；nlerp 插值含完整公式）；**圆弧/Bézier 明确推迟**，未知 type 必须拒绝（§1.2/1.3/1.4） | G0/G1/G2/G3 全方言能力；圆弧原生支持（G-code 本身） |
| 3 | 工艺参数 | profile 集中声明：lpbf 六参数 + deposition 三参数 + 前后等待；机器特化走**命名空间 profile codec**（§4.1、§2.3） | 参数散布在 gcode 行内（M104/M106/回抽…）+ 尾部 CONFIG_BLOCK 文本快照（586 参数实测）（§5.4/§8.1） |
| 4 | 参数调制 | **modifier 归一化**：profile 声明 [min,max]，几何只带 0–1 因子（e/f/g/h ≤4 个/profile，constant/linear/nonlinear+`<sub>` 支持点）；`value = min + f·(max−min)`；消费者**装载期**即可断言包络并拒绝不支持的调制（§4.2） | 无对应机制——动态值直接写死在 gcode 里（如流速变化的 E 值序列） |
| 5 | 完整性校验 | 无每层数字校验和；依赖 ZIP CRC + **语义前置校验**（modifier sanity check 必须做、lasersource/同步组引用不解析即拒绝）（§4.2/§4.5） | 四层：ZIP CRC32 → **plate_N.gcode.md5**（解压后完整字节，32 位大写 hex；执行任何指令前校验，不符拒绝启动）→ 四方交叉验证（plater_id↔index↔gcode_file↔.rels+条目）→ 语义解析；MD5 非防篡改签名（§5.5/§8.3） |
| 6 | 机型绑定 | profile codec + required-extensions；`tp:toolpathid` 多方案选择（§4.6） | 机型预设决定 G-code 方言；机型信息多来源交叉（slice_info `printer_model_id` 等，§8.2） |
| 7 | 多对象/多盘 | 一个 toolpathresource = 一托盘；层跨全托，`partid`（层内局部表→build item UUID）把几何归属到对象（§3.2 Note、Part II §1.1.1） | 盘为单位：`plate_N` 系列按**原始盘号**命名（可稀疏）；对象信息在 slice_info/plate_N.json |
| 8 | 并行执行 | 多激光各自轨道：同激光严格文档序、跨激光可并行、`lasersync` 同步屏障（无独立 sync segment）（§1.2.2） | 单线程解释器语义，无并行概念 |
| 9 | 厂商扩展 | 三条正道：命名空间属性/profile codec、`tp:toolpathdata` 元数据容器、层内 `<data>`；**禁**外联/DTD/XInclude/CDATA/二进制/脚本，未知命名空间忽略且 round-trip 保留（§2.3/§4.4） | Metadata 目录自由约定 + 厂商关系类型（bambulab/snapmaker 两代 URI 后缀兼容）（§2/§5.2） |
| 10 | 时间预估 | `timeprediction`/`jumpprediction` 逐 segment 微秒级，明示不得用于安全关键时序（§1.2） | 盘级秒数（slice_info `prediction`）；gcode 头部亦有 estimated printing time（§5.3/§8.1） |
| 11 | 缩略图 | 无专门规定，沿用 Core 第 6 章 | 自成体系：包级封面（Auxiliaries）+ 盘级渲染族 plate_N.png/_small/no_light/top/pick（§4/§5.7–5.10） |
| 12 | 元数据快照 | `tp:toolpathdata`（provenance/slicer 设置快照/QA）——**明文降级为不参与执行语义**（§4.4） | project_settings.config（500+ 键 JSON）+ 内嵌预设——同样明文"固件不据此重新切片"（§5.11/§8.1） |
| 13 | 生态状态 | RC，无消费级落地；预留二进制编码扩展命名空间（`…/binary/2023/05`）（App. C） | 量产多年，Bambu 生态通用 |

## 5. 互转映射可行性（本文分析，非规范结论）

**gcode.3mf → Toolpath 方向**（fork 若要做"联盟格式导出器"）：

| gcode.3mf 侧 | Toolpath 侧 | 可行性 |
|---|---|---|
| `;LAYER_CHANGE` 逐层注释 | 每层一个 layer part | 直接映射（切片器侧本就有层概念） |
| 墙/填充/支撑几何（G1 段 + `;TYPE:` 标记） | loop / polyline / hatch segment | 可映射，但 G2/G3 圆弧必须离散化（RC 无弧线原语） |
| E 轴流量动态 | modifier 调制 `depositionspeed`（nonlinear + `<sub>` 支持点） | 语义可表达，精度取决于支撑点密度 |
| `EXCLUDE_OBJECT_DEFINE` 对象标记 | `partid` → build item UUID（需 Production 扩展 UUID） | 可映射，但 gcode.3mf 的 3dmodel.model 是空壳——导出器须补全几何与 UUID，等于重做非 SkipModel 导出 |
| CONFIG_BLOCK / project_settings 快照 | `tp:toolpathdata` | 可放，但降级为非执行元数据 |
| **温度/风扇/回抽/自定义宏**（M104/M106/自定义 G-code） | **无标准参数位** | 只能进自定义 profile codec（参与执行）或 toolpathdata（不参与执行）；无联盟互操作性 |

结论：几何与层结构可无损度较高地映射；**FFF 工艺语义的完整表达仍需大量自定义 codec**，此时"联盟格式"退化为带标准几何骨架的私有格式—— interoperability 收益有限。

**Toolpath → gcode.3mf 方向**：需要机器端编译器把 profile+几何编译成指令流——这正是 RC 设计意图（LPBF 机器厂商的活），FFF 切片器不需要做。

## 6. 对 fork 的含义与建议

1. **短期（~Published 前）无行动项**：RC + LPBF 生态先行 + Production 硬依赖，消费级 FFF 场景无 adopting 压力。
2. **观察项 O1**（建议列入阶段二后的跟踪清单，非 P0）：关注 RC → Published 演进与三件事——deposition 参数集是否扩容（决定 FFF 表达力）、Binary Encoding 扩展落地（决定大文件实用性）、联盟内消费级厂商动向。
3. **规范文本可借鉴两点**：① modifier 的"包络声明 + 归一化因子"思路，若将来 gcode.3mf 要加动态参数能力，可参考；② RC 对厂商元数据容器的安全禁令清单（禁外联/CDATA/二进制/脚本）比我们现有约定更系统，可吸收进阶段二的安全禁入项（呼应 docs/04 Q11 凭据字段的讨论）。
4. **命名巧合**：`.gcode.3mf` 双扩展恰好符合 Core 1.4.0 §2.2.1 厂商约定（`.vendor.3mf`）的精神，无需改动。

## 7. 事实核对记录（防以讹传讹）

| 疑点 | 核对结果 | 出处 |
|---|---|---|
| `.build.3mf` 与 `.toolpath.3mf` 语义分工 | Core 1.4.0 §2.2.1：`.build.3mf` = "complete build plate or tray of models, **prepared for a specific printer**"；`.toolpath.3mf` = "machine-specific toolpath data"（保留名，当前无规范认领）。Toolpath RC 选 `.build.3mf` 自洽——其包是"含托盘装配+刀具路径的成品件包" | Core §2.2.1/§2.2.2；RC Ch.3 |
| 命名空间从 microsoft.com 迁到 3mf.io？ | 是。Toolpath 现用 `schemas.3mf.io/.../2026/03`；旧 `schemas.microsoft.com/.../toolpath/2019/05` **禁止生产、读取兼容**。Boolean Operations 1.1.0（2024-03）同样完成迁移 | RC App. C 弃用注记；Boolean §Document Conventions |
| RC 发布时间 | 修订史仅一条：1.0.0 First published version, September 3, 2026；状态 Release Candidate | RC Change History |
| 为何强制 Production 扩展 | 全链路 UUID 引用（resource/profile/build item）依赖 Production 提供；RC 明文 "MUST also include the production extension as required" | RC Preface/Ch.1 |
| 二进制编码是否已有 | 无。RC 仅预留 `bin:` 命名空间（`…/binary/2023/05`）给未来的 Binary Encoding extension，ASCII XML 是当前唯一编码 | RC §1.1 Note、App. C |

## 8. 引用

- 3MF Consortium, *3MF Toolpath Extension — Specification & Reference Guide* 1.0.0 RC（2026-09-03）。本地副本：`C:\Users\snapmaker\Downloads\3MF Toolpath Extension.md`
- 3MF Consortium, *3MF Core Specification* 1.4.0（2025-02-06）§2.2。本地副本：`C:\Users\snapmaker\Downloads\3MF-Core-Specification.md`
- 本仓库《gcode.3mf 规范 v0.9.9 版》《gcode_3mf 文件格式标准》《gcode_3mf 目录与文件详解》（`wiki/specification/gcode.3mf/`）
