# nozzle_type

> 所在界面：打印机设置 → Basic information → Accessory
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/basic information/printer_basic_information_accessory.md` 的「Nozzle type」小节（2026-10-28），英文原文，待本地化校对。

---

## Nozzle type

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `nozzle_type[extruder_idx]`.  
[Type](option_type#list-types): `Choice list`.  
[Options](option_type#choice): `undefine, hardened_steel, stainless_steel, tungsten_carbide, brass`.  
[CLI Example](cli_mode#setting-overrides): `--nozzle-type=undefine`.  
The metallic material of the nozzle: This determines the abrasive resistance of the nozzle and what kind of filament can be printed.
