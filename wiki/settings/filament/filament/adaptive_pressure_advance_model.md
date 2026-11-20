# adaptive_pressure_advance_model

> Location: Filament → Filament → Flow ratio and Pressure Advance → Adaptive pressure advance measurements (beta)

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `adaptive_pressure_advance_model`.  
[Type](../../../general_settings/option_type.md#list-types): `Text list`.  
[Default](../../../general_settings/option_type.md#default-value): `0,0,0\n0,0,0`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--adaptive-pressure-advance-model=value`.  

Add sets of **pressure advance** (PA) values, the **volumetric flow speeds** and **accelerations** they were measured at, separated by a comma.  
One set of values per line. For example:

```json
[PA 1],[FLOW 1],[ACCELERATION 1]
[PA 2],[FLOW 2],[ACCELERATION 2]
...
[PA n],[FLOW n],[ACCELERATION n]
```

```json
0.04,3.96,3000
0.033,3.96,10000
0.029,7.91,3000
0.026,7.91,10000
```
