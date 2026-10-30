# spiral_finishing_flow_ratio

> Location: Process → Others → Special mode

---

### Spiral finishing flow ratio

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `spiral_finishing_flow_ratio`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--spiral-finishing-flow-ratio=1`.  
Sets the finishing flow ratio when ending the spiral. Normally, the flow scales from 100% to 0% during the last loop, which can lead to under-extrusion at the end.  
Use this to control the ending and ensure consistent extrusion. Only applied when [Use relative E distances](../../printer/basic_information/printer_basic_information_advanced.md#use-relative-e-distances) is enabled.
