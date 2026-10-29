# nozzle_diameter

> 所在界面：打印机设置 → Extruder N → Size
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/extruder/printer_extruder_basic_information.md` 的「Nozzle diameter」小节（2026-10-28），英文原文，待本地化校对。

---

## Nozzle diameter

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `nozzle_diameter[extruder_idx]`.  
[Type](option_type#list-types): `Float list`.  
[CLI Example](cli_mode#setting-overrides): `--nozzle-diameter=1`.  
The diameter of the nozzle for each extruder.  

> [!TIP]
> You can use different nozzle diameters for each extruder to achieve different print qualities and speeds.  
> Follow the [Mixed Nozzle Sizes](mixed_nozzle_sizes) guide for more information on how to use this feature.
