# brim_ears_max_angle

> Location: Process → Others → Brim

---

#### Ear max angle

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `brim_ears_max_angle`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--brim-ears-max-angle=1`.  
Angle threshold (degrees) used to decide where mouse ears may be placed:

- 0° — disabled; no mouse ears are generated.
- Between 0° and 180° — ears are created at features with local angles sharper (smaller) than the threshold.
- 180° — ears are allowed on almost any non-straight feature.
