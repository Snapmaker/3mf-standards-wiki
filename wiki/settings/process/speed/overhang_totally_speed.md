# overhang_totally_speed

> Location: Process → Speed → Overhang speed → 100%
> Status: placeholder — to be completed.
> This key shares the "Slow down for overhang" row with `overhang_1_4_speed` / `overhang_2_4_speed` / `overhang_3_4_speed` / `overhang_4_4_speed` (5th column, labeled 100%).

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `overhang_totally_speed`.  
[Type](../../../general_settings/option_type.md#list-types): `Float or Percentage list`.  
[Default](../../../general_settings/option_type.md#default-value): `10`.  
[Unit](../../../general_settings/option_type.md#unit): `mm/s or %`.  
[Range](../../../general_settings/option_type.md#range): `≥ 0`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--overhang-totally-speed=1`.  

Speed of 100% overhang wall which has 0 overlap with the lower layer.

A % value is [`outer_wall_speed`](outer_wall_speed.md).

## Notes

Printing speed for fully-floating outer walls (0 overlap with the layer below, 100% overhang) — the most extreme level. Stock OrcaSlicer treats such walls as bridges (applying the 75% level and capping at bridge speed); Snapmaker Orca splits this into its own level.

<!-- TODO: relation to bridge_speed -->
