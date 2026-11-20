# enable_overlap_area_carving

> Location: Process → Others → Special mode
> Status: placeholder — fork-added parameter, to be completed.

## Basic information

- Label: Carve overlaps by per-layer slice area
- Mode: Developer
- Type: Boolean
- Default: false

> Tooltip: When enabled, overlaps between multi-extruder parts are carved with the new algorithm: on each layer, the part with the smaller slice area owns the overlap, keeping small details intact inside larger bodies. Developer option.

## Notes

Toggles the carving algorithm for overlap regions between multi-extruder parts. When enabled, the new algorithm applies: on each layer, **the part with the smaller cross-section area** owns the overlap, so details of small parts inside large parts are preserved. Located in the Special mode group after [`slicing_mode`](slicing_mode.md).

<!-- TODO: illustrations of old vs new algorithm, impact on assembly tolerances -->
