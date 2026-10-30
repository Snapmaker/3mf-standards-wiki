# ironing_flow

> Location: Process → Quality → Ironing

---

## Flow

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `ironing_flow`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Percentage`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--ironing-flow=20%`.  
The amount of material to extrude during ironing.  
It is a percentage of the flow of a normal layer height. A lower value will result in a smoother finish but may not cover the surface completely. A higher value may cover the surface better but can lead to over-extrusion or a rougher finish.

A lower layer height may require higher flow due to less volumetric extrusion per distance.
