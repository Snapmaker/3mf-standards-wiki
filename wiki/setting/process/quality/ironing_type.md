# ironing_type

> Location: Process → Quality → Ironing

---

## Type

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `ironing_type`.  
[Type](../../../general_settings/option_type.md#choice): `Choice`.  
[Options](../../../general_settings/option_type.md#choice): `no ironing, top, topmost, solid`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--ironing-type="no ironing"`.  
This setting controls which layers are ironed.

- **All top surfaces**: All [top surfaces](../../process/strength/strength_settings_top_bottom_shells.md) will be ironed. This is the most common setting and is used to smooth out the top layers of the print.  
  ![ironing-top-surfaces](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/ironing/ironing-top-surfaces.png?raw=true)
- **Topmost surface only**: Only the last [top layer](../../process/strength/strength_settings_top_bottom_shells.md) of each object will be ironed. This is useful for prints where only the last layer needs to be smoothed.  
  ![ironing-topmost-surface](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/ironing/ironing-topmost-surface.png?raw=true)
- **All solid layers**: All solid layers, including [internal solid infill](../../process/strength/strength_settings_infill.md#internal-solid-infill) and [top layers](../../process/strength/strength_settings_top_bottom_shells.md), will be ironed. This can be useful for prints that require a very smooth finish on all solid surfaces but may increase print time significantly.  
    ![ironing-all-solid-layers](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/ironing/ironing-all-solid-layers.png?raw=true)
