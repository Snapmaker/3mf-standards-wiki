# resolution

> Location: Process → Quality → Precision

---

## Resolution

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `resolution`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--resolution=1`.  
The G-code path is generated after simplifying the contour of models to avoid too many points and G-code lines.  
Smaller values mean higher resolution and more time to slice. If you are slicing big models on machines with low processing power, you may want to increase this value to speed up the slicing process.
