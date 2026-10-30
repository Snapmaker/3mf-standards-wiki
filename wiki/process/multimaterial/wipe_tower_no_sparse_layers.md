# wipe_tower_no_sparse_layers

> Location: Process → Multimaterial → Prime tower
> 显隐条件（初步梳理，待校对）：仅非 BBL 机型显示

---

## No sparse layers

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `wipe_tower_no_sparse_layers`.  
[Type](../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--wipe-tower-no-sparse-layers=1`.  

> [!IMPORTANT]
> NEW FEATURE: **No sparse layers on every prime tower type**  
> Available in: [Nightly builds](https://github.com/OrcaSlicer/OrcaSlicer/releases/tag/nightly-builds) or Releases greater than **2.4.2**.

If enabled, the prime tower is not printed on layers with no tool changes. The tower therefore stays low while the model keeps rising, and on the next layer that does have a tool change the extruder travels back down to print it.

Because the tower ends up below the model, the toolhead has to reach down to it past everything already printed. Orca checks the plate for that before slicing and rejects layouts where the nozzle, the toolhead body or the gantry rod would hit an object, highlighting the collision area and the height limit it would exceed. Move the model further from the tower, lower its height, or turn this option off.

> [!TIP]
> If the plate layout can't avoid a collision, [Combine sparse layers](#combine-sparse-layers) also cuts the time spent on sparse tower layers while keeping the tower level with the model.

> [!NOTE]
> This option has no effect when [smooth timelapse](../../process/others/others_settings_special_mode.md#timelapse) or [clumping detection](../../process/others/others_settings_special_mode.md#enable-clumping-detection) is enabled, because both keep every sparse layer of the tower. Enabling it while smooth timelapse is selected switches timelapse to traditional, and selecting smooth timelapse turns this option off.
