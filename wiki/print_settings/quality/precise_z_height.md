# precise_z_height

> 所在界面：工艺设置 → Quality → Precision
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_precision.md` 的「Precise Z Height」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Precise Z Height

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `precise_z_height`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--precise-z-height=1`.  
This feature ensures the accurate Z height of the model after slicing, even if the model height is not a multiple of the [layer height](quality_settings_layer_height).

For example, slicing a 20mm x 20mm x 20.1mm cube with a layer height of 0.2mm would typically result in a final height of 20.2mm due to the layer height increments.

By enabling this parameter, the layer height of the last five layers is adjusted so that the final sliced height matches the actual object height, resulting in an accurate 20.1mm (as shown in the picture).

- **Precise Z Height Off**

  ![PreciseZOff](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Precision/PreciseZOff.png?raw=true)

- **Precise Z Height On**

  ![PreciseZOn](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/Precision/PreciseZOn.png?raw=true)
