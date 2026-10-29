# spiral_finishing_flow_ratio

> 所在界面：工艺设置 → Others → Special mode
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_special_mode.md` 的「Spiral finishing flow ratio」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Spiral finishing flow ratio

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `spiral_finishing_flow_ratio`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--spiral-finishing-flow-ratio=1`.  
Sets the finishing flow ratio when ending the spiral. Normally, the flow scales from 100% to 0% during the last loop, which can lead to under-extrusion at the end.  
Use this to control the ending and ensure consistent extrusion. Only applied when [Use relative E distances](printer_basic_information_advanced#use-relative-e-distances) is enabled.
