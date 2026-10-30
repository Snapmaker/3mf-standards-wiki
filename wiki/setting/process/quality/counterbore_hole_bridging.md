# counterbore_hole_bridging

> Location: Process → Quality → Bridging

---

## Bridge Counterbore hole

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `counterbore_hole_bridging`.  
[Type](../../../general_settings/option_type.md#choice): `Choice`.  
[Options](../../../general_settings/option_type.md#choice): `none, partiallybridge, sacrificiallayer`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--counterbore-hole-bridging=none`.  
When printing counterbore holes, the unsupported area can lead to sagging or poor surface quality. Also, the perimeters of the counterbore hole may not be printed correctly, leading to gaps or weak points in the structure.

This option creates bridges for counterbore holes, allowing them to be printed without support.  
Available modes include:

- **None:** No bridge is created.  
  ![bridge-counterbore-none](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/bridging/bridge-counterbore-none.png?raw=true)
- **Partially bridged:** Only a part of the unsupported area will be bridged, creating a supporting layer for the next layer.  
  ![bridge-counterbore-partially](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/bridging/bridge-counterbore-partially.gif?raw=true)
- **Sacrificial layer:** A full sacrificial bridge layer is created. This will close the counterbore hole, allowing the next layer to be printed without sagging. The sacrificial layer must be broken through after printing.  
  ![bridge-counterbore-sacrificial](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/bridging/bridge-counterbore-sacrificial.png?raw=true)
