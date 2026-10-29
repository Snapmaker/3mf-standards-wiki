# enable_support

> 所在界面：工艺设置 → Support → Support
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_support.md` 的「Support」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

# Support

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `enable_support`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--enable-support=1`.  
Support structures are used in 3D printing to provide stability to overhangs and complex geometries.

- [Type](#type)
    - [Normal](#normal)
    - [Tree](#tree)
        - [Support critical regions only](#support-critical-regions-only)
    - [Auto](#auto)
    - [Manual](#manual)
- [Style](#style)
    - [Grid](#grid)
    - [Snug](#snug)
    - [Organic](#organic)
    - [Tree Slim](#tree-slim)
    - [Tree Strong](#tree-strong)
    - [Tree Hybrid](#tree-hybrid)
- [Threshold angle](#threshold-angle)
- [Threshold overlap](#threshold-overlap)
- [Initial layer density](#initial-layer-density)
- [Initial layer expansion](#initial-layer-expansion)
- [On build plate only](#on-build-plate-only)
- [Ignore small overhangs](#ignore-small-overhangs)
