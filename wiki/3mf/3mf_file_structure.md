# 3mf 内部文件组成与作用

← [Wiki 首页](../home.md)

> 面向新人的入门文档：一个 3mf 里有哪些文件、各自干什么用。
> 日期：2026-10-15　依据：切片软件实际导出样本解包实测。字段级细节与证据见 [研发内部资料](../../docs/)（文档 01–04）。

## 1. 3mf 是什么

一个 **zip 压缩包**（OPC 格式，同 docx/xlsx 的打包方式），后缀改成 `.zip` 就能直接解压查看。内容分三层：

| 层 | 位置 | 管什么 |
|---|---|---|
| 容器层 | 包根目录的 2 个 xml | 包的"目录页"和"入口" |
| 几何层 | `3D/` | 三维模型本身 |
| 配置层 | `Metadata/` | 打印参数、对象信息、缩略图等 |

## 2. 目录结构总览

```
xxx.3mf
├─ [Content_Types].xml              ← 文件类型注册表
├─ _rels/.rels                      ← 包入口声明
├─ 3D/
│  ├─ 3dmodel.model                 ← 主模型文件（必有）
│  ├─ _rels/3dmodel.model.rels      ← 外部网格登记（仅工程文件）
│  └─ Objects/立方体_1.model …      ← 网格数据（仅工程文件）
└─ Metadata/
   ├─ project_settings.config       ← 全局打印设置（必有）
   ├─ model_settings.config         ← 对象与打印板信息（必有）
   ├─ slice_info.config             ← 预留，目前是空的（必有）
   ├─ plate_1.png 等                ← 打印板预览图（按盘数）
   └─ …                             ← 其他按需出现的文件，见 §3
```

## 3. 每个文件的作用

### 3.1 必有文件

| 文件 | 格式 | 作用 |
|---|---|---|
| `[Content_Types].xml` | XML | 包的"目录页"：告诉读取软件每种扩展名代表什么类型（model 是三维模型、png 是图片…） |
| `_rels/.rels` | XML | 包的"入口声明"：指出主模型文件在哪、封面缩略图是哪张。不认识它的软件就打不开这个包 |
| `3D/3dmodel.model` | XML | **主模型**：列出所有对象，以及每个对象实例摆在打印板的什么位置（坐标变换） |
| `Metadata/project_settings.config` | JSON | **全局打印设置**：层高、速度、耗材、机器等所有参数，500 多项键值对 |
| `Metadata/model_settings.config` | XML | **对象与打印板信息**：每个对象叫什么、用哪个耗材槽、哪些实例放在哪块打印板上 |
| `Metadata/slice_info.config` | XML | 为切片结果摘要预留的位置，目前实测是空壳 |

### 3.2 按需出现的文件

| 文件 | 何时出现 | 作用 |
|---|---|---|
| `plate_N.png` / `plate_no_light_N.png` / `top_N.png` / `pick_N.png` / `plate_1_small.png` | 有打印板就有 | 板面预览图 5 种：常规渲染、无光照、俯视、拾取示意、封面小图 |
| `machine_settings_N.config` / `process_settings_N.config` / `filament_settings_N.config` | 导出时嵌入预设 | 预设快照：机器、工艺、耗材三类的完整参数，供他人生成同配置 |
| `custom_gcode_per_layer.xml` | 设置了按层 G-code | 记录"打到第几层时插入什么 G-code" |
| `layer_heights_profile.txt` / `layer_config_ranges.xml` | 用了变层高 | 变层高的轮廓与区间 |
| `brim_ear_points.txt` | 用了象耳裙边 | 象耳的锚点坐标 |
| `plate_N.json` | 新版本（2.4.0+）导出 | 打印板布局摘要：尺寸、耗材、喷嘴等 |
| `Auxiliaries/` | 用户附加了图片 | 用户放进去的图片等资源，原样保留 |

### 3.3 仅工程文件才有

| 文件 | 作用 |
|---|---|
| `3D/Objects/<对象名>_<编号>.model` | 网格本体（顶点+三角形），每个对象一个文件；主模型里只留引用 |
| `3D/_rels/3dmodel.model.rels` | 登记上面这些网格文件，读取端据此找到它们 |

## 4. 文件之间如何关联

```
_rels/.rels ──入口──▶ 3D/3dmodel.model ──编号对应──▶ model_settings.config
                         │                              │
                         └──引用──▶ Objects/*.model      └──记录──▶ 哪些对象在哪块板、缩略图文件名
```

- **入口**：读取软件先看 `_rels/.rels`，找到主模型文件。
- **编号对应**：主模型里每个对象有编号（id），`model_settings.config` 用相同编号描述同一对象——一边是几何，一边是属性。
- **参数覆盖**：全局参数在 `project_settings.config`；单个对象可覆盖其中某些参数（记录在 `model_settings.config`），对象内部零件还可再覆盖，越里层优先级越高。

## 5. 为什么有的 3mf 有 Objects/ 文件夹，有的没有

同一个软件有两种保存方式，几何数据的存放位置不同：

| | 直接保存工程 | 导出通用 3MF |
|---|---|---|
| 网格位置 | 拆成 `3D/Objects/` 下每对象一个文件 | 全部内嵌在 `3dmodel.model` 里 |
| 附加标记 | 带对象 UUID（生产扩展） | 无任何私有扩展，第三方兼容性最好 |
| 打印配置 `Metadata/` | 完整保留 | **同样完整保留**（并未因"通用"而精简） |

其他行业软件（如 Bambu Studio 原生导出）的工程文件也采用"外拆到 Objects/"的方式，两种形态都符合 3MF 标准。

---
深入阅读（研发内部资料）：

- 配置文件全景盘点：[01-现状盘点-切片软件3mf配置文件](../../docs/01-现状盘点-切片软件3mf配置文件.md)
- 字段字典与对账：[02-字段字典对账-project_settings](../../docs/02-字段字典对账-project_settings.md)
- 对象与预设细节：[03-现状盘点-model_settings与嵌入预设](../../docs/03-现状盘点-model_settings与嵌入预设.md)
- 已知问题清单：[04-问题清单-切片软件团队对齐](../../docs/04-问题清单-切片软件团队对齐.md)
