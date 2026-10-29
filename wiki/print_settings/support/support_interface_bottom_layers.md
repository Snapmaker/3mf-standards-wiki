# support_interface_bottom_layers

> 所在界面：工艺设置 → Support → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_advanced.md` 的「Interface layers」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`support_interface_top_layers`（各另有独立文档）。

---

## Interface layers

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `support_interface_top_layers`, `support_interface_bottom_layers`.  
[Type](option_type#integer-float-percentage): `Integer`.  
[CLI Example](cli_mode#setting-overrides): `--support-interface-top-layers=1` (same pattern for the other variables above).  
The number of interface layers.

The number you set is the total thickness of the dense interface, counted in printed layers and including the layer that faces the model. Set `1` and you get a single dense layer; set `3` and you get three. More layers give a flatter, better supported surface but take longer to print and are harder to peel off.

The top and bottom interfaces are set separately:

- **Top interface layers** (`support_interface_top_layers`) are the layers printed under an overhang, below the [Z distance](#z-distance) gap. These are the ones that determine the finish of the supported surface.
- **Bottom interface layers** (`support_interface_bottom_layers`) are the layers printed where a support lands on top of the model, protecting that surface from the support body. `Same as top` reuses the top value. You can use bottom interfaces on their own, with top interface layers set to `0`.

With both set to `0` there is no interface at all: the support prints all the way through with the [Base Pattern](#base-pattern), which is fastest and easiest to remove but leaves the roughest overhangs.

> [!TIP]
> When the interface has its own filament assigned, this number also decides how the layers are shared between the two materials. See [Interface filament transitions](support_settings_filament#interface-filament-transitions).
