# additional_cooling_fan_speed

> Location: Filament → Cooling → Auxiliary part cooling fan
> 显隐条件（初步梳理，待校对）：需打印机启用辅助风扇后显示

---

### Auxiliary part cooling fan

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `additional_cooling_fan_speed`.  
[Type](../../../general_settings/option_type.md#list-types): `Integer list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--additional-cooling-fan-speed=1`.  
Set the speed for the auxiliary part-cooling fan if your printer provides one (see [auxiliary part-cooling fan](../../printer/basic_information/printer_basic_information_accessory.md#auxiliary-part-cooling-fan)). The auxiliary fan runs during printing but is disabled for the initial layers defined by [No cooling for the first](#no-cooling-for-the-first).

G-code command: `M106 P2 S(0-255)`
