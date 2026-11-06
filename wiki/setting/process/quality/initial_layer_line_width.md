# initial_layer_line_width

> Location: Process → Quality → Line width

---

### First Layer

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `initial_layer_line_width`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float or Percentage`.  
[Default](../../../general_settings/option_type.md#default-value): `0`.  
[Range](../../../general_settings/option_type.md#range): `0–1000` mm or %.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--initial-layer-line-width=20%`.  
A wider first layer (with a higher [first layer height](../../process/quality/initial_layer_print_height.md)) improves bed adhesion and compensates for uneven build surfaces.  
First layer line width also overrides [Brim's](../../process/others/brim_type.md) and [Skirt's](../../process/others/skirt_loops.md) line width.
