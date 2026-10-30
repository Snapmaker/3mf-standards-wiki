# infill_combination_max_layer_height

> Location: Process → Strength → Advanced

---

### Max layer height

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `infill_combination_max_layer_height`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float or Percentage`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--infill-combination-max-layer-height=20%`.  
Maximum layer height for the combined sparse infill.  
Set it to 0 or 100% to use the nozzle diameter (for maximum reduction in print time), or to a value of ~80% to maximize sparse infill strength.

The number of layers over which infill is combined is derived by dividing this value by the layer height and rounding down to a whole number.

Use either absolute mm values (e.g., 0.32mm for a 0.4mm nozzle) or percentages (e.g., 80%). This value must not be larger than the nozzle diameter.
