# slow_down_for_layer_cooling

> Location: Filament → Cooling → Part cooling fan

---

### Slow printing down for better layer cooling

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `slow_down_for_layer_cooling`.  
[Type](../../../general_settings/option_type.md#list-types): `Boolean list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--slow-down-for-layer-cooling=1`.  
Enable this option to slow printing speed down to ensure that the final layer time is not shorter than the **Layer time** threshold in [Max fan speed threshold](#max-fan-speed-threshold), so that the layer can be cooled for a longer time. This can improve the quality for small details.

This happens after the [print speeds](../../process/speed/speed_settings_other_layers_speed.md) have been applied, so on small or fast layers the printed speed can be lower than the value you set. It applies to every layer, including the first one, and the slowed-down speeds are written into the G-code: you can see them in the Preview **Speed** view.

The slowdown has a floor: no extrusion is slowed down below the filament's [Min print speed](#min-print-speed).  
If the layer would still be shorter than the Layer time with every extrusion at Min print speed, everything that can be slowed down prints at Min print speed and the layer finishes earlier than the target.

> [!TIP]
> If small layers still don't cool enough because Min print speed was reached, print several copies of the part at once so each layer takes longer.
