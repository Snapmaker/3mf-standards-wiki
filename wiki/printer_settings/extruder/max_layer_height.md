# max_layer_height

> 所在界面：打印机设置 → Extruder N → Layer height limits
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/extruder/printer_extruder_basic_information.md` 的「Extruder Layer Height Limits」小节（2026-10-28），英文原文，待本地化校对。

---

## Extruder Layer Height Limits

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `extruder_printable_height[extruder_idx]`, `min_layer_height[extruder_idx]`, `max_layer_height[extruder_idx]`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--extruder-printable-height=1` (same pattern for the other variables above).  
Min and max layer height limits for the extruder. These settings are used when adaptive layer height is enabled.
