# extruder_offset

> 所在界面：打印机设置 → Extruder N → Position
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/extruder/printer_extruder_basic_information.md` 的「Extruder offset Position」小节（2026-10-28），英文原文，待本地化校对。

---

## Extruder offset Position

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `extruder_offset[extruder_idx]`.  
[Type](option_type#list-types): `Point list`.  
[CLI Example](cli_mode#setting-overrides): `--extruder-offset=100,100`.  
If your firmware doesn't handle the extruder displacement you need the G-code to take it into account. This option lets you specify the displacement of each extruder with respect to the first one. It expects positive coordinates (they will be subtracted from the XY coordinate).
