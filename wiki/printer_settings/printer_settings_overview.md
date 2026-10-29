# 打印机设置参数总览

> 页面结构按 fork 实际 UI（Tab.cpp `TabPrinter::build_fff` / `build_unregular_pages`，2026-10-28 核实）。
> 每键一文档；✅ = 内容拷贝自上游 OrcaSlicer wiki，🚧 = 占位待补。

## Basic information（`basic_information/`）

- ✅ [`printable_area`](basic_information/printable_area.md)（Printable space）
- ✅ [`bed_exclude_area`](basic_information/bed_exclude_area.md)（Printable space）
- ✅ [`printable_height`](basic_information/printable_height.md)（Printable space）
- ✅ [`support_multi_bed_types`](basic_information/support_multi_bed_types.md)（Printable space）
- ✅ [`nozzle_volume`](basic_information/nozzle_volume.md)（Printable space）
- ✅ [`best_object_pos`](basic_information/best_object_pos.md)（Printable space）
- ✅ [`z_offset`](basic_information/z_offset.md)（Printable space）
- ✅ [`preferred_orientation`](basic_information/preferred_orientation.md)（Printable space）
- ✅ [`printer_structure`](basic_information/printer_structure.md)（Advanced）
- ✅ [`gcode_flavor`](basic_information/gcode_flavor.md)（Advanced）
- ✅ [`pellet_modded_printer`](basic_information/pellet_modded_printer.md)（Advanced）
- ✅ [`bbl_use_printhost`](basic_information/bbl_use_printhost.md)（Advanced）
- ✅ [`disable_m73`](basic_information/disable_m73.md)（Advanced）
- ✅ [`thumbnails`](basic_information/thumbnails.md)（Advanced）
- ✅ [`use_relative_e_distances`](basic_information/use_relative_e_distances.md)（Advanced）
- ✅ [`use_firmware_retraction`](basic_information/use_firmware_retraction.md)（Advanced）
- ✅ [`time_cost`](basic_information/time_cost.md)（Advanced）
- ✅ [`fan_speedup_time`](basic_information/fan_speedup_time.md)（Cooling Fan）
- ✅ [`fan_speedup_overhangs`](basic_information/fan_speedup_overhangs.md)（Cooling Fan）
- ✅ [`fan_kickstart`](basic_information/fan_kickstart.md)（Cooling Fan）
- ✅ [`extruder_clearance_radius`](basic_information/extruder_clearance_radius.md)（Extruder Clearance）
- ✅ [`extruder_clearance_height_to_rod`](basic_information/extruder_clearance_height_to_rod.md)（Extruder Clearance）
- ✅ [`extruder_clearance_height_to_lid`](basic_information/extruder_clearance_height_to_lid.md)（Extruder Clearance）
- ✅ [`bed_mesh_min`](basic_information/bed_mesh_min.md)（Adaptive bed mesh）
- ✅ [`bed_mesh_max`](basic_information/bed_mesh_max.md)（Adaptive bed mesh）
- ✅ [`bed_mesh_probe_distance`](basic_information/bed_mesh_probe_distance.md)（Adaptive bed mesh）
- ✅ [`adaptive_bed_mesh_margin`](basic_information/adaptive_bed_mesh_margin.md)（Adaptive bed mesh）
- ✅ [`nozzle_type`](basic_information/nozzle_type.md)（Accessory）
- ✅ [`nozzle_hrc`](basic_information/nozzle_hrc.md)（Accessory）
- ✅ [`auxiliary_fan`](basic_information/auxiliary_fan.md)（Accessory）
- ✅ [`support_chamber_temp_control`](basic_information/support_chamber_temp_control.md)（Accessory）
- ✅ [`support_air_filtration`](basic_information/support_air_filtration.md)（Accessory）

## Machine G-code（`machine_gcode/`）

- ✅ [`machine_start_gcode`](machine_gcode/machine_start_gcode.md)（Machine start G-code）
- ✅ [`machine_end_gcode`](machine_gcode/machine_end_gcode.md)（Machine end G-code）
- ✅ [`printing_by_object_gcode`](machine_gcode/printing_by_object_gcode.md)（Printing by object G-code）
- ✅ [`before_layer_change_gcode`](machine_gcode/before_layer_change_gcode.md)（Before layer change G-code）
- ✅ [`layer_change_gcode`](machine_gcode/layer_change_gcode.md)（Layer change G-code）
- ✅ [`time_lapse_gcode`](machine_gcode/time_lapse_gcode.md)（Timelapse G-code）
- ✅ [`change_filament_gcode`](machine_gcode/change_filament_gcode.md)（Change filament G-code）
- ✅ [`change_extrusion_role_gcode`](machine_gcode/change_extrusion_role_gcode.md)（Change extrusion role G-code）
- ✅ [`machine_pause_gcode`](machine_gcode/machine_pause_gcode.md)（Pause G-code）
- ✅ [`template_custom_gcode`](machine_gcode/template_custom_gcode.md)（Template Custom G-code）

## Multimaterial（`multimaterial/`）

- ✅ [`single_extruder_multi_material`](multimaterial/single_extruder_multi_material.md)（Single extruder multi-material setup）
- ✅ [`extruders_count`](multimaterial/extruders_count.md)（Single extruder multi-material setup）
- ✅ [`manual_filament_change`](multimaterial/manual_filament_change.md)（Single extruder multi-material setup）
- ✅ [`purge_in_prime_tower`](multimaterial/purge_in_prime_tower.md)（Wipe tower）
- ✅ [`enable_filament_ramming`](multimaterial/enable_filament_ramming.md)（Wipe tower）
- 🚧 [`ramming_line_width_ratio`](multimaterial/ramming_line_width_ratio.md)（Wipe tower）
- 🚧 [`enable_change_pressure_when_wiping`](multimaterial/enable_change_pressure_when_wiping.md)（Wipe tower）
- 🚧 [`ramming_pressure_advance_value`](multimaterial/ramming_pressure_advance_value.md)（Wipe tower）
- ✅ [`cooling_tube_retraction`](multimaterial/cooling_tube_retraction.md)（Single extruder multi-material parameters）
- ✅ [`cooling_tube_length`](multimaterial/cooling_tube_length.md)（Single extruder multi-material parameters）
- ✅ [`parking_pos_retraction`](multimaterial/parking_pos_retraction.md)（Single extruder multi-material parameters）
- ✅ [`extra_loading_move`](multimaterial/extra_loading_move.md)（Single extruder multi-material parameters）
- ✅ [`high_current_on_filament_swap`](multimaterial/high_current_on_filament_swap.md)（Single extruder multi-material parameters）
- ✅ [`machine_load_filament_time`](multimaterial/machine_load_filament_time.md)（Advanced）
- ✅ [`machine_unload_filament_time`](multimaterial/machine_unload_filament_time.md)（Advanced）
- ✅ [`machine_tool_change_time`](multimaterial/machine_tool_change_time.md)（Advanced）
- 🚧 [`tool_change_temprature_wait`](multimaterial/tool_change_temprature_wait.md)（Advanced）

## Extruder N（`extruder/`）

- ✅ [`nozzle_diameter`](extruder/nozzle_diameter.md)（Size）
- ✅ [`min_layer_height`](extruder/min_layer_height.md)（Layer height limits）
- ✅ [`max_layer_height`](extruder/max_layer_height.md)（Layer height limits）
- ✅ [`extruder_offset`](extruder/extruder_offset.md)（Position）
- ✅ [`retraction_length`](extruder/retraction_length.md)（Retraction）
- ✅ [`retract_restart_extra`](extruder/retract_restart_extra.md)（Retraction）
- ✅ [`retraction_speed`](extruder/retraction_speed.md)（Retraction）
- ✅ [`deretraction_speed`](extruder/deretraction_speed.md)（Retraction）
- ✅ [`retraction_minimum_travel`](extruder/retraction_minimum_travel.md)（Retraction）
- ✅ [`retract_when_changing_layer`](extruder/retract_when_changing_layer.md)（Retraction）
- ✅ [`wipe`](extruder/wipe.md)（Retraction）
- ✅ [`wipe_distance`](extruder/wipe_distance.md)（Retraction）
- ✅ [`retract_before_wipe`](extruder/retract_before_wipe.md)（Retraction）
- ✅ [`retract_length_toolchange`](extruder/retract_length_toolchange.md)（Retraction when switching material）
- ✅ [`retract_restart_extra_toolchange`](extruder/retract_restart_extra_toolchange.md)（Retraction when switching material）
- 🚧 [`long_retractions_when_cut`](extruder/long_retractions_when_cut.md)（Retraction when switching material）
- 🚧 [`retraction_distances_when_cut`](extruder/retraction_distances_when_cut.md)（Retraction when switching material）
- ✅ [`retract_lift_enforce`](extruder/retract_lift_enforce.md)（Z-Hop）
- ✅ [`z_hop_types`](extruder/z_hop_types.md)（Z-Hop）
- ✅ [`z_hop`](extruder/z_hop.md)（Z-Hop）
- 🚧 [`z_hop_when_prime`](extruder/z_hop_when_prime.md)（Z-Hop）
- ✅ [`travel_slope`](extruder/travel_slope.md)（Z-Hop）
- ✅ [`retract_lift_above`](extruder/retract_lift_above.md)（Z-Hop）
- ✅ [`retract_lift_below`](extruder/retract_lift_below.md)（Z-Hop）

## Motion ability（`motion_ability/`）

- ✅ [`emit_machine_limits_to_gcode`](motion_ability/emit_machine_limits_to_gcode.md)（Advanced）
- ✅ [`resonance_avoidance`](motion_ability/resonance_avoidance.md)（Resonance Avoidance）
- ✅ [`min_resonance_avoidance_speed`](motion_ability/min_resonance_avoidance_speed.md)（Resonance Avoidance）
- ✅ [`max_resonance_avoidance_speed`](motion_ability/max_resonance_avoidance_speed.md)（Resonance Avoidance）
- ✅ [`machine_max_speed_x`](motion_ability/machine_max_speed_x.md)（Speed limitation）
- ✅ [`machine_max_speed_y`](motion_ability/machine_max_speed_y.md)（Speed limitation）
- ✅ [`machine_max_speed_z`](motion_ability/machine_max_speed_z.md)（Speed limitation）
- ✅ [`machine_max_speed_e`](motion_ability/machine_max_speed_e.md)（Speed limitation）
- ✅ [`machine_max_acceleration_x`](motion_ability/machine_max_acceleration_x.md)（Acceleration limitation）
- ✅ [`machine_max_acceleration_y`](motion_ability/machine_max_acceleration_y.md)（Acceleration limitation）
- ✅ [`machine_max_acceleration_z`](motion_ability/machine_max_acceleration_z.md)（Acceleration limitation）
- ✅ [`machine_max_acceleration_e`](motion_ability/machine_max_acceleration_e.md)（Acceleration limitation）
- ✅ [`machine_max_acceleration_extruding`](motion_ability/machine_max_acceleration_extruding.md)（Acceleration limitation）
- ✅ [`machine_max_acceleration_retracting`](motion_ability/machine_max_acceleration_retracting.md)（Acceleration limitation）
- ✅ [`machine_max_acceleration_travel`](motion_ability/machine_max_acceleration_travel.md)（Acceleration limitation）
- ✅ [`machine_max_jerk_x`](motion_ability/machine_max_jerk_x.md)（Jerk limitation）
- ✅ [`machine_max_jerk_y`](motion_ability/machine_max_jerk_y.md)（Jerk limitation）
- ✅ [`machine_max_jerk_z`](motion_ability/machine_max_jerk_z.md)（Jerk limitation）
- ✅ [`machine_max_jerk_e`](motion_ability/machine_max_jerk_e.md)（Jerk limitation）
- ✅ [`machine_max_junction_deviation`](motion_ability/machine_max_junction_deviation.md)（Jerk limitation）

## Notes（`notes/`）

- 🚧 [`printer_notes`](notes/printer_notes.md)（Notes）

共 104 键：96 拷贝 / 8 占位。
