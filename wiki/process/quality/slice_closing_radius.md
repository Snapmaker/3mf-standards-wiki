# slice_closing_radius

> Location: Process → Quality → Precision

---

## Slice gap closing radius

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `slice_closing_radius`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--slice-closing-radius=1`.  
Cracks smaller than 2x the gap closing radius are filled during the triangle mesh slicing.  
The gap closing operation may reduce the final print resolution, therefore it is advisable to keep the value reasonably low.
