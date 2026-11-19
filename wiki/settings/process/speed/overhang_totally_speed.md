# overhang_totally_speed

> Location: Process → Speed → Overhang speed
> Status: placeholder — to be completed.
> This key shares the "Slow down for overhang" row with `overhang_1_4_speed` / `overhang_2_4_speed` / `overhang_3_4_speed` / `overhang_4_4_speed` (5th column, labeled 100%).

## Basic information (from fork `PrintConfig.cpp`)

- Label: 100% (full_label same)
- Type: coFloatsOrPercents, unit mm/s or % (% relative to [`outer_wall_speed`](outer_wall_speed.md)), min 0
- Default: 10
- Mode: Advanced

> Tooltip (original): Speed of 100% overhang wall which has 0 overlap with the lower layer.

## Notes

Printing speed for fully-floating outer walls (0 overlap with the layer below, 100% overhang) — the most extreme level. Upstream treats such walls as bridges (applying the 75% level and capping at bridge speed); the fork splits this into its own level.

(To add: relation to bridge_speed)
