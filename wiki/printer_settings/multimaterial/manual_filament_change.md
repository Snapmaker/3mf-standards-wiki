# manual_filament_change

> 所在界面：打印机设置 → Multimaterial → Single extruder multi-material setup
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/multimaterial/printer_multimaterial_setup.md` 的「Manual Filament Change」小节（2026-10-28），英文原文，待本地化校对。

---

## Manual Filament Change

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `manual_filament_change`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--manual-filament-change=1`.  
Manual filament change is a feature that allows the user to change the filament during the print. This can be useful for multi-material prints or when changing colors. The user can specify the position and timing of the filament change, as well as the speed and distance of the ramming process.  
Enable this option to omit the custom Change filament G-code only at the beginning of the print. The tool change command (e.g., T0) will be skipped throughout the entire print. This is useful for manual multi-material printing, where we use M600/PAUSE to trigger the manual filament change action.
