# wall_generator

> Location: Process → Quality → Wall generator

---

# Wall Generator

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `wall_generator`.  
[Type](../../general_settings/option_type.md#choice): `Choice`.  
[Options](../../general_settings/option_type.md#choice): `classic, arachne`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--wall-generator=classic`.  
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
