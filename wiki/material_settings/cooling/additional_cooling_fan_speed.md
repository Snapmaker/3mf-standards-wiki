# additional_cooling_fan_speed

> 所在界面：耗材设置 → Cooling → Auxiliary part cooling fan
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/cooling/material_cooling.md` 的「Auxiliary part cooling fan」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 显隐条件（初步梳理，待校对）：需打印机启用辅助风扇后显示

---

### Auxiliary part cooling fan

[Mode](option_mode): `Simple`.  
[Variable](built_in_placeholders_variables): `additional_cooling_fan_speed`.  
[Type](option_type#list-types): `Integer list`.  
[CLI Example](cli_mode#setting-overrides): `--additional-cooling-fan-speed=1`.  
Set the speed for the auxiliary part-cooling fan if your printer provides one (see [auxiliary part-cooling fan](printer_basic_information_accessory#auxiliary-part-cooling-fan)). The auxiliary fan runs during printing but is disabled for the initial layers defined by [No cooling for the first](#no-cooling-for-the-first).

G-code command: `M106 P2 S(0-255)`
