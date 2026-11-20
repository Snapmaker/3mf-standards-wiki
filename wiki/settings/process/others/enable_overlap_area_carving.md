# enable_overlap_area_carving

> Location: Process → Others → Special mode → Carve overlaps by per-layer slice area
> Status: placeholder — fork-added parameter, to be completed.

---

[Mode](../../../general_settings/option_mode.md): `Developer`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `enable_overlap_area_carving`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[Default](../../../general_settings/option_type.md#default-value): `false`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--enable-overlap-area-carving=1`.  

When enabled, overlaps between multi-extruder parts are carved with the new algorithm: on each layer, the part with the smaller slice area owns the overlap, keeping small details intact inside larger bodies. Developer option.

## Notes

Toggles the carving algorithm for overlap regions between multi-extruder parts. When enabled, the new algorithm applies: on each layer, **the part with the smaller cross-section area** owns the overlap, so details of small parts inside large parts are preserved. Located in the Special mode group after [`slicing_mode`](slicing_mode.md).

<!-- TODO: illustrations of old vs new algorithm, impact on assembly tolerances -->
