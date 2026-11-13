# adaptive_pressure_advance_model

> Location: Filament → Filament → Flow ratio and Pressure Advance

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
