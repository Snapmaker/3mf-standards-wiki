# default_acceleration

> Location: Process → Speed → Acceleration

---

## Normal printing

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `default_acceleration`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--default-acceleration=1`.  
The default acceleration for both normal printing and travel after the first layer.

> [!NOTE]
> If this value is set to 0, Orca doesn't send acceleration commands, so the printer's own acceleration is used and the other acceleration settings are disabled.
