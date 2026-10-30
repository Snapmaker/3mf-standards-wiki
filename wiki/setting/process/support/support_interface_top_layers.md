# support_interface_top_layers

> Location: Process → Support → Advanced
> 本小节同时涵盖：`support_interface_bottom_layers`（各另有独立文档）。

---

## Interface layers

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `support_interface_top_layers`, `support_interface_bottom_layers`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Integer`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--support-interface-top-layers=1` (same pattern for the other variables above).  
The number of interface layers.

The number you set is the total thickness of the dense interface, counted in printed layers and including the layer that faces the model. Set `1` and you get a single dense layer; set `3` and you get three. More layers give a flatter, better supported surface but take longer to print and are harder to peel off.

The top and bottom interfaces are set separately:

- **Top interface layers** (`support_interface_top_layers`) are the layers printed under an overhang, below the [Z distance](#z-distance) gap. These are the ones that determine the finish of the supported surface.
- **Bottom interface layers** (`support_interface_bottom_layers`) are the layers printed where a support lands on top of the model, protecting that surface from the support body. `Same as top` reuses the top value. You can use bottom interfaces on their own, with top interface layers set to `0`.

With both set to `0` there is no interface at all: the support prints all the way through with the [Base Pattern](#base-pattern), which is fastest and easiest to remove but leaves the roughest overhangs.

> [!TIP]
> When the interface has its own filament assigned, this number also decides how the layers are shared between the two materials. See [Interface filament transitions](../../process/support/support_settings_filament.md#interface-filament-transitions).
