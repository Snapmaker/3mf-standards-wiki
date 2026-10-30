# support_base_pattern

> Location: Process → Support → Advanced

---

## Base Pattern

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `support_base_pattern`.  
[Type](../../general_settings/option_type.md#choice): `Choice`.  
[Options](../../general_settings/option_type.md#choice): `default, rectilinear, rectilinear-grid, honeycomb, lightning, hollow`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--support-base-pattern=default`.  
Line pattern for the base of the support.

`Default` depends on the support type: normal supports use `Rectilinear`, and tree supports are left `Hollow`, with only the branch walls printed. With the [Tree Hybrid](../../process/support/support_settings_support.md#tree-hybrid) style, `Default` fills the parts printed as normal support with `Rectilinear` and leaves the branches hollow, while choosing `Rectilinear` fills the branches too.
