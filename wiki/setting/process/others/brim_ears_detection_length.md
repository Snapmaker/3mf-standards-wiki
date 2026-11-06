# brim_ears_detection_length

> Location: Process → Others → Brim

---

#### Ear detection radius

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `brim_ears_detection_length`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[Default](../../../general_settings/option_type.md#default-value): `1`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0` mm.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--brim-ears-detection-length=1`.  
The geometry is decimated before sharp angles are detected.  
This parameter sets the minimum deviation length used for the decimation.  
Set to 0 to disable.
