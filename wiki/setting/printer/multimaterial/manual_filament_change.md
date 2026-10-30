# manual_filament_change

> Location: Printer → Multimaterial → Single extruder multi-material setup

---

## Manual Filament Change

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `manual_filament_change`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--manual-filament-change=1`.  
Manual filament change is a feature that allows the user to change the filament during the print. This can be useful for multi-material prints or when changing colors. The user can specify the position and timing of the filament change, as well as the speed and distance of the ramming process.  
Enable this option to omit the custom Change filament G-code only at the beginning of the print. The tool change command (e.g., T0) will be skipped throughout the entire print. This is useful for manual multi-material printing, where we use M600/PAUSE to trigger the manual filament change action.
