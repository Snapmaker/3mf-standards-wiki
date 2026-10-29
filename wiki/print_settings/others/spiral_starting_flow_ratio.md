# spiral_starting_flow_ratio

> 所在界面：工艺设置 → Others → Special mode
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_special_mode.md` 的「Spiral starting flow ratio」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Spiral starting flow ratio

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `spiral_starting_flow_ratio`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--spiral-starting-flow-ratio=1`.  
Sets the starting flow ratio when transitioning from the last bottom layer to the spiral.  
Normally, the flow scales from 0% to 100% during the first loop, which can sometimes cause under-extrusion at the start.  
Adjust this to fine-tune the transition and prevent issues. Only applied when [Use relative E distances](printer_basic_information_advanced#use-relative-e-distances) is enabled.
