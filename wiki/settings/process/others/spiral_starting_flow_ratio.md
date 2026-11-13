# spiral_starting_flow_ratio

> Location: Process → Others → Special mode

---

### Spiral starting flow ratio

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `spiral_starting_flow_ratio`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[Default](../../../general_settings/option_type.md#default-value): `0`.  
[Range](../../../general_settings/option_type.md#range): `0–1`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--spiral-starting-flow-ratio=1`.  
Sets the starting flow ratio when transitioning from the last bottom layer to the spiral.  
Normally, the flow scales from 0% to 100% during the first loop, which can sometimes cause under-extrusion at the start.  
Adjust this to fine-tune the transition and prevent issues. Only applied when [Use relative E distances](../../printer/basic_information/use_relative_e_distances.md) is enabled.
