# adaptive_pressure_advance_model

> 所在界面：耗材设置 → Filament → Flow ratio and Pressure Advance
> 来源：拷贝自上游 OrcaSlicer wiki `material_settings/filament/material_flow_ratio_and_pressure_advance.md` 的「Adaptive pressure advance measurements (beta)」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

#### Adaptive pressure advance measurements (beta)

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
