# extra_perimeters_on_overhangs

> Location: Process → Quality → Overhangs

---

## Extra perimeters on overhangs

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `extra_perimeters_on_overhangs`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--extra-perimeters-on-overhangs=1`.  
Create additional perimeter (overhang wall) paths over steep overhangs and areas where bridges cannot be anchored.

This option only works when [Detect overhang walls](#detect-overhang-wall) is enabled, even though it stays visible and editable when that option is off.

![extra-perimeters-on-overhangs](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/overhangs/extra-perimeters-on-overhangs.png?raw=true)
