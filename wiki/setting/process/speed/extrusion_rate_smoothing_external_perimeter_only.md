# extrusion_rate_smoothing_external_perimeter_only

> Location: Process → Speed → Advanced

---

## Apply only on external features

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `extrusion_rate_smoothing_external_perimeter_only`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--extrusion-rate-smoothing-external-perimeter-only=1`.  
Applies extrusion rate smoothing only to outer walls and overhang walls, leaving the flow of all other features unchanged. This can reduce artifacts caused by sharp speed transitions on visible overhangs without slowing down features that won't be seen.  
This option is only shown when Extrusion rate smoothing is greater than 0, and it is disabled by default.
