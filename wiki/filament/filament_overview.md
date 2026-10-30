# 耗材设置参数总览

> 页面结构按 fork 实际 UI（Tab.cpp `TabFilament::build` / `add_filament_overrides_page`，2026-10-28 核实）。
> 每键一文档；✅ = 内容拷贝自上游 OrcaSlicer wiki，🚧 = 占位待补，🔗 = 交叉引用（回抽覆盖参数见 printer_settings）。

## Filament（`filament/`）

- ✅ [`filament_type`](filament/filament_type.md)（Basic information）
- ✅ [`filament_vendor`](filament/filament_vendor.md)（Basic information）
- ✅ [`filament_soluble`](filament/filament_soluble.md)（Basic information）
- ✅ [`filament_is_support`](filament/filament_is_support.md)（Basic information）
- ✅ [`required_nozzle_HRC`](filament/required_nozzle_HRC.md)（Basic information）
- ✅ [`default_filament_colour`](filament/default_filament_colour.md)（Basic information）
- ✅ [`filament_diameter`](filament/filament_diameter.md)（Basic information）
- ✅ [`filament_density`](filament/filament_density.md)（Basic information）
- ✅ [`filament_shrink`](filament/filament_shrink.md)（Basic information）
- ✅ [`filament_shrinkage_compensation_z`](filament/filament_shrinkage_compensation_z.md)（Basic information）
- ✅ [`filament_cost`](filament/filament_cost.md)（Basic information）
- ✅ [`temperature_vitrification`](filament/temperature_vitrification.md)（Basic information）
- ✅ [`idle_temperature`](filament/idle_temperature.md)（Basic information）
- ✅ [`filament_tower_interface_pre_extrusion_dist`](filament/filament_tower_interface_pre_extrusion_dist.md)（Basic information）
- ✅ [`filament_tower_interface_pre_extrusion_length`](filament/filament_tower_interface_pre_extrusion_length.md)（Basic information）
- ✅ [`filament_tower_interface_print_temp`](filament/filament_tower_interface_print_temp.md)（Basic information）
- ✅ [`filament_tower_ironing_area`](filament/filament_tower_ironing_area.md)（Basic information）
- ✅ [`filament_adhesiveness_category`](filament/filament_adhesiveness_category.md)（Basic information）
- 🚧 [`nozzle_temperature_range_low`](filament/nozzle_temperature_range_low.md)（Basic information）
- 🚧 [`nozzle_temperature_range_high`](filament/nozzle_temperature_range_high.md)（Basic information）
- 🚧 [`pellet_flow_coefficient`](filament/pellet_flow_coefficient.md)（Flow ratio and Pressure Advance）
- ✅ [`filament_flow_ratio`](filament/filament_flow_ratio.md)（Flow ratio and Pressure Advance）
- ✅ [`enable_pressure_advance`](filament/enable_pressure_advance.md)（Flow ratio and Pressure Advance）
- ✅ [`pressure_advance`](filament/pressure_advance.md)（Flow ratio and Pressure Advance）
- ✅ [`adaptive_pressure_advance`](filament/adaptive_pressure_advance.md)（Flow ratio and Pressure Advance）
- ✅ [`adaptive_pressure_advance_overhangs`](filament/adaptive_pressure_advance_overhangs.md)（Flow ratio and Pressure Advance）
- ✅ [`adaptive_pressure_advance_bridges`](filament/adaptive_pressure_advance_bridges.md)（Flow ratio and Pressure Advance）
- ✅ [`adaptive_pressure_advance_model`](filament/adaptive_pressure_advance_model.md)（Flow ratio and Pressure Advance）
- ✅ [`chamber_temperature`](filament/chamber_temperature.md)（Print chamber temperature）
- ✅ [`activate_chamber_temp_control`](filament/activate_chamber_temp_control.md)（Print chamber temperature）
- ✅ [`nozzle_temperature_initial_layer`](filament/nozzle_temperature_initial_layer.md)（Print temperature）
- ✅ [`nozzle_temperature`](filament/nozzle_temperature.md)（Print temperature）
- ✅ [`supertack_plate_temp_initial_layer`](filament/supertack_plate_temp_initial_layer.md)（Bed temperature）
- ✅ [`supertack_plate_temp`](filament/supertack_plate_temp.md)（Bed temperature）
- ✅ [`cool_plate_temp_initial_layer`](filament/cool_plate_temp_initial_layer.md)（Bed temperature）
- ✅ [`cool_plate_temp`](filament/cool_plate_temp.md)（Bed temperature）
- ✅ [`textured_cool_plate_temp_initial_layer`](filament/textured_cool_plate_temp_initial_layer.md)（Bed temperature）
- ✅ [`textured_cool_plate_temp`](filament/textured_cool_plate_temp.md)（Bed temperature）
- ✅ [`eng_plate_temp_initial_layer`](filament/eng_plate_temp_initial_layer.md)（Bed temperature）
- ✅ [`eng_plate_temp`](filament/eng_plate_temp.md)（Bed temperature）
- ✅ [`hot_plate_temp_initial_layer`](filament/hot_plate_temp_initial_layer.md)（Bed temperature）
- ✅ [`hot_plate_temp`](filament/hot_plate_temp.md)（Bed temperature）
- ✅ [`textured_plate_temp_initial_layer`](filament/textured_plate_temp_initial_layer.md)（Bed temperature）
- ✅ [`textured_plate_temp`](filament/textured_plate_temp.md)（Bed temperature）
- ✅ [`graphic_effect_plate_temp_initial_layer`](filament/graphic_effect_plate_temp_initial_layer.md)（Bed temperature）
- 🚧 [`graphic_effect_plate_temp`](filament/graphic_effect_plate_temp.md)（Bed temperature）
- ✅ [`filament_max_volumetric_speed`](filament/filament_max_volumetric_speed.md)（Volumetric speed limitation）

## Cooling（`cooling/`）

- ✅ [`close_fan_the_first_x_layers`](cooling/close_fan_the_first_x_layers.md)（Cooling for specific layer）
- ✅ [`full_fan_speed_layer`](cooling/full_fan_speed_layer.md)（Cooling for specific layer）
- ✅ [`fan_min_speed`](cooling/fan_min_speed.md)（Part cooling fan）
- ✅ [`fan_cooling_layer_time`](cooling/fan_cooling_layer_time.md)（Part cooling fan）
- ✅ [`fan_max_speed`](cooling/fan_max_speed.md)（Part cooling fan）
- ✅ [`slow_down_layer_time`](cooling/slow_down_layer_time.md)（Part cooling fan）
- ✅ [`reduce_fan_stop_start_freq`](cooling/reduce_fan_stop_start_freq.md)（Part cooling fan）
- ✅ [`slow_down_for_layer_cooling`](cooling/slow_down_for_layer_cooling.md)（Part cooling fan）
- ✅ [`dont_slow_down_outer_wall`](cooling/dont_slow_down_outer_wall.md)（Part cooling fan）
- ✅ [`slow_down_min_speed`](cooling/slow_down_min_speed.md)（Part cooling fan）
- ✅ [`enable_overhang_bridge_fan`](cooling/enable_overhang_bridge_fan.md)（Part cooling fan）
- ✅ [`overhang_fan_threshold`](cooling/overhang_fan_threshold.md)（Part cooling fan）
- ✅ [`overhang_fan_speed`](cooling/overhang_fan_speed.md)（Part cooling fan）
- ✅ [`internal_bridge_fan_speed`](cooling/internal_bridge_fan_speed.md)（Part cooling fan）
- ✅ [`support_material_interface_fan_speed`](cooling/support_material_interface_fan_speed.md)（Part cooling fan）
- ✅ [`ironing_fan_speed`](cooling/ironing_fan_speed.md)（Part cooling fan）
- ✅ [`additional_cooling_fan_speed`](cooling/additional_cooling_fan_speed.md)（Auxiliary part cooling fan）
- ✅ [`activate_air_filtration`](cooling/activate_air_filtration.md)（Exhaust fan）
- ✅ [`during_print_exhaust_fan_speed`](cooling/during_print_exhaust_fan_speed.md)（Exhaust fan）
- ✅ [`complete_print_exhaust_fan_speed`](cooling/complete_print_exhaust_fan_speed.md)（Exhaust fan）

## Setting Overrides（`setting_overrides/`）

- 🔗 [`filament_retraction_length`](setting_overrides/filament_retraction_length.md)（Retraction）
- 🔗 [`filament_z_hop`](setting_overrides/filament_z_hop.md)（Retraction）
- 🔗 [`filament_z_hop_types`](setting_overrides/filament_z_hop_types.md)（Retraction）
- 🔗 [`filament_retract_lift_above`](setting_overrides/filament_retract_lift_above.md)（Retraction）
- 🔗 [`filament_retract_lift_below`](setting_overrides/filament_retract_lift_below.md)（Retraction）
- 🔗 [`filament_retract_lift_enforce`](setting_overrides/filament_retract_lift_enforce.md)（Retraction）
- 🔗 [`filament_retraction_speed`](setting_overrides/filament_retraction_speed.md)（Retraction）
- 🔗 [`filament_deretraction_speed`](setting_overrides/filament_deretraction_speed.md)（Retraction）
- 🔗 [`filament_retract_restart_extra`](setting_overrides/filament_retract_restart_extra.md)（Retraction）
- 🔗 [`filament_retraction_minimum_travel`](setting_overrides/filament_retraction_minimum_travel.md)（Retraction）
- 🔗 [`filament_retract_when_changing_layer`](setting_overrides/filament_retract_when_changing_layer.md)（Retraction）
- 🔗 [`filament_wipe`](setting_overrides/filament_wipe.md)（Retraction）
- 🔗 [`filament_wipe_distance`](setting_overrides/filament_wipe_distance.md)（Retraction）
- 🔗 [`filament_retract_before_wipe`](setting_overrides/filament_retract_before_wipe.md)（Retraction）
- 🔗 [`filament_long_retractions_when_cut`](setting_overrides/filament_long_retractions_when_cut.md)（Retraction）
- 🔗 [`filament_retraction_distances_when_cut`](setting_overrides/filament_retraction_distances_when_cut.md)（Retraction）
- 🔗 [`filament_retract_length_toolchange`](setting_overrides/filament_retract_length_toolchange.md)（Retraction）
- 🔗 [`filament_retract_restart_extra_toolchange`](setting_overrides/filament_retract_restart_extra_toolchange.md)（Retraction）

## Advanced（`advanced/`）

- ✅ [`filament_start_gcode`](advanced/filament_start_gcode.md)（Filament start G-code）
- ✅ [`filament_end_gcode`](advanced/filament_end_gcode.md)（Filament end G-code）

## Multimaterial（`multimaterial/`）

- ✅ [`filament_minimal_purge_on_wipe_tower`](multimaterial/filament_minimal_purge_on_wipe_tower.md)（Wipe tower parameters）
- ✅ [`filament_loading_speed_start`](multimaterial/filament_loading_speed_start.md)（Tool change parameters with single extruder MM printers）
- ✅ [`filament_loading_speed`](multimaterial/filament_loading_speed.md)（Tool change parameters with single extruder MM printers）
- ✅ [`filament_unloading_speed_start`](multimaterial/filament_unloading_speed_start.md)（Tool change parameters with single extruder MM printers）
- ✅ [`filament_unloading_speed`](multimaterial/filament_unloading_speed.md)（Tool change parameters with single extruder MM printers）
- ✅ [`filament_toolchange_delay`](multimaterial/filament_toolchange_delay.md)（Tool change parameters with single extruder MM printers）
- ✅ [`filament_cooling_moves`](multimaterial/filament_cooling_moves.md)（Tool change parameters with single extruder MM printers）
- ✅ [`filament_cooling_initial_speed`](multimaterial/filament_cooling_initial_speed.md)（Tool change parameters with single extruder MM printers）
- ✅ [`filament_cooling_final_speed`](multimaterial/filament_cooling_final_speed.md)（Tool change parameters with single extruder MM printers）
- ✅ [`filament_stamping_loading_speed`](multimaterial/filament_stamping_loading_speed.md)（Tool change parameters with single extruder MM printers）
- ✅ [`filament_stamping_distance`](multimaterial/filament_stamping_distance.md)（Tool change parameters with single extruder MM printers）
- ✅ [`filament_ramming_parameters`](multimaterial/filament_ramming_parameters.md)（Tool change parameters with single extruder MM printers）
- ✅ [`filament_multitool_ramming`](multimaterial/filament_multitool_ramming.md)（Tool change parameters with multi extruder MM printers）
- ✅ [`filament_multitool_ramming_volume`](multimaterial/filament_multitool_ramming_volume.md)（Tool change parameters with multi extruder MM printers）
- ✅ [`filament_multitool_ramming_flow`](multimaterial/filament_multitool_ramming_flow.md)（Tool change parameters with multi extruder MM printers）

## Dependencies（`dependencies/`）

- ✅ [`compatible_printers`](dependencies/compatible_printers.md)（Compatible printers）
- ✅ [`compatible_printers_condition`](dependencies/compatible_printers_condition.md)（Compatible printers）
- ✅ [`compatible_prints`](dependencies/compatible_prints.md)（Compatible process profiles）
- ✅ [`compatible_prints_condition`](dependencies/compatible_prints_condition.md)（Compatible process profiles）

## Notes（`notes/`）

- 🚧 [`filament_notes`](notes/filament_notes.md)（Notes）

共 107 键：84 拷贝 / 5 占位 / 18 交叉引用。
