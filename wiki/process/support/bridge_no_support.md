# bridge_no_support

> Location: Process → Support → Advanced

---

## Don't support bridges

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `bridge_no_support`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--bridge-no-support=1`.  
Don't support bridge areas, which would otherwise make the support very large. Bridges can usually be printed directly without support if they are not very long.

This option is only shown for normal supports. Tree supports use [Max bridge length](#max-bridge-length) instead.
