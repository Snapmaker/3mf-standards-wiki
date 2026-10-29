# ironing_type

> 所在界面：工艺设置 → Quality → Ironing
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_ironing.md` 的「Type」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Type

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `ironing_type`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `no ironing, top, topmost, solid`.  
[CLI Example](cli_mode#setting-overrides): `--ironing-type="no ironing"`.  
This setting controls which layers are ironed.

- **All top surfaces**: All [top surfaces](strength_settings_top_bottom_shells) will be ironed. This is the most common setting and is used to smooth out the top layers of the print.  
  ![ironing-top-surfaces](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/ironing/ironing-top-surfaces.png?raw=true)
- **Topmost surface only**: Only the last [top layer](strength_settings_top_bottom_shells) of each object will be ironed. This is useful for prints where only the last layer needs to be smoothed.  
  ![ironing-topmost-surface](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/ironing/ironing-topmost-surface.png?raw=true)
- **All solid layers**: All solid layers, including [internal solid infill](strength_settings_infill#internal-solid-infill) and [top layers](strength_settings_top_bottom_shells), will be ironed. This can be useful for prints that require a very smooth finish on all solid surfaces but may increase print time significantly.  
    ![ironing-all-solid-layers](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/ironing/ironing-all-solid-layers.png?raw=true)
