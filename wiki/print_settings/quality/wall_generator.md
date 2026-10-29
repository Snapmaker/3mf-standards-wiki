# wall_generator

> 所在界面：工艺设置 → Quality → Wall generator
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_wall_generator.md` 的「Wall Generator」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

# Wall Generator

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `wall_generator`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `classic, arachne`.  
[CLI Example](cli_mode#setting-overrides): `--wall-generator=classic`.  
The Wall Generator defines how the outer and inner walls (perimeters) of the model are printed.

- [Classic](#classic)
- [Arachne](#arachne)
    - [Wall transitioning threshold angle](#wall-transitioning-threshold-angle)
    - [Wall transitioning filter margin](#wall-transitioning-filter-margin)
    - [Wall transitioning length](#wall-transitioning-length)
    - [Wall distribution count](#wall-distribution-count)
    - [Minimum wall width](#minimum-wall-width)
        - [First layer minimum wall width](#first-layer-minimum-wall-width)
    - [Minimum feature size](#minimum-feature-size)
    - [Minimum wall length](#minimum-wall-length)
    - [Maximum wall resolution](#maximum-wall-resolution)
    - [Maximum wall deviation](#maximum-wall-deviation)
