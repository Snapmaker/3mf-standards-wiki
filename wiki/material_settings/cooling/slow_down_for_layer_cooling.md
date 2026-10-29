# slow_down_for_layer_cooling

> 所在界面：耗材设置 → Cooling → Part cooling fan
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/cooling/material_cooling.md` 的「Slow printing down for better layer cooling」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Slow printing down for better layer cooling

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `slow_down_for_layer_cooling`.  
[Type](option_type#list-types): `Boolean list`.  
[CLI Example](cli_mode#setting-overrides): `--slow-down-for-layer-cooling=1`.  
Enable this option to slow printing speed down to ensure that the final layer time is not shorter than the **Layer time** threshold in [Max fan speed threshold](#max-fan-speed-threshold), so that the layer can be cooled for a longer time. This can improve the quality for small details.

This happens after the [print speeds](speed_settings_other_layers_speed) have been applied, so on small or fast layers the printed speed can be lower than the value you set. It applies to every layer, including the first one, and the slowed-down speeds are written into the G-code: you can see them in the Preview **Speed** view.

The slowdown has a floor: no extrusion is slowed down below the filament's [Min print speed](#min-print-speed).  
If the layer would still be shorter than the Layer time with every extrusion at Min print speed, everything that can be slowed down prints at Min print speed and the layer finishes earlier than the target.

> [!TIP]
> If small layers still don't cool enough because Min print speed was reached, print several copies of the part at once so each layer takes longer.
