# independent_support_layer_height

> Location: Process → Support → Advanced

---

## Independent support layer height

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `independent_support_layer_height`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--independent-support-layer-height=1`.  
Support layers use a layer height independent of the object layers. This allows a custom Z gap and saves print time. This option is ignored when a prime tower is printed, and it is not available with the Organic tree support style.

Turning this on changes the height of the support layers, not their number: you still get exactly the [Interface layers](#interface-layers) you asked for, including with the `Tree Slim`, `Tree Strong` and `Tree Hybrid` styles.
