# raft_layers

> 所在界面：工艺设置 → Support → Raft
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_raft.md` 的「Raft」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。
> 本小节同时涵盖：`raft_contact_distance`（各另有独立文档）。

---

# Raft

[Mode](option_mode): `Advanced`.  
[Variables](built_in_placeholders_variables): `raft_layers`, `raft_contact_distance`, `raft_expansion`.  
[Type](option_type): `raft_layers` (Integer), `raft_contact_distance` (Float), `raft_expansion` (Float).  
[CLI Example](cli_mode#setting-overrides): `--raft-layers=1` (`raft_layers` shown; other variables above follow their own type).  
A raft is a platform of support material printed under the object. The object is printed on the raft instead of on the build plate, and the raft is removed after printing.

A raft helps when:

- The material tends to warp or lift at the corners, like ABS, ASA, PC or Nylon.
- The object touches the bed with a small area, thin features or sharp edges that would not stay attached.
- The build plate is uneven or worn: the raft absorbs small height variations before the first object layer.

In exchange, the bottom of the object is rougher, the print takes more time and material, and the raft has to be removed.

> [!TIP]
> If the problem is only adhesion or warping, try a [brim](others_settings_brim) first. It is faster, uses less material and keeps the bottom surface clean.

- [How a raft is built](#how-a-raft-is-built)
- [Layers](#layers)
- [Contact Z distance](#contact-z-distance)
- [Expansion](#expansion)
- [Interaction with other settings](#interaction-with-other-settings)
