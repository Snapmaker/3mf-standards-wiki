# raft_layers

> Location: Process → Support → Raft → Raft
> Also in this section: `raft_contact_distance` (each documented on its own page).

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `raft_layers`.  
[Type](../../../general_settings/option_type.md): Integer.  
[Default](../../../general_settings/option_type.md#default-value): `0`.  
[Unit](../../../general_settings/option_type.md#unit): `layers`.  
[Range](../../../general_settings/option_type.md#range): `0–100`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--raft-layers=1`.  

A raft is a platform of support material printed under the object. The object is printed on the raft instead of on the build plate, and the raft is removed after printing.

A raft helps when:

- The material tends to warp or lift at the corners, like ABS, ASA, PC or Nylon.
- The object touches the bed with a small area, thin features or sharp edges that would not stay attached.
- The build plate is uneven or worn: the raft absorbs small height variations before the first object layer.

In exchange, the bottom of the object is rougher, the print takes more time and material, and the raft has to be removed.

> [!TIP]
> If the problem is only adhesion or warping, try a [brim](../../process/others/brim_type.md) first. It is faster, uses less material and keeps the bottom surface clean.

- [How a raft is built](#how-a-raft-is-built)
- [Layers](#layers)
- [Contact Z distance](#contact-z-distance)
- [Expansion](#expansion)
- [Interaction with other settings](#interaction-with-other-settings)
