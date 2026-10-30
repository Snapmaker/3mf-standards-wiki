# bed_exclude_area

> Location: Printer → Basic information → Printable space

---

## Excluded bed area

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `bed_exclude_area`.  
[Type](../../general_settings/option_type.md#list-types): `Point list`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--bed-exclude-area=100,100`.  
Unprintable area in XY plane. For example, X1 Series printers use the front left corner to cut filament during filament change. The area is expressed as polygon by points in following format: "XxY, XxY, ..."  
It keeps models and printed material out of the area, but the toolhead can still travel through it, as the X1 does to cut the filament. To also keep the toolhead's moves out, set [Toolhead collision volumes](#toolhead-collision-volumes).
