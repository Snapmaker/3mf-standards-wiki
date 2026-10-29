# print_order

> 所在界面：工艺设置 → Others → Special mode
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_special_mode.md` 的「Intra-layer order」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Intra-layer order

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `print_order`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `default, as_obj_list, best_of, snake`.  
[CLI Example](cli_mode#setting-overrides): `--print-order=default`.  
Determines the order in which object instances are visited within a single layer, which controls how much travel is spent moving between them.

Shorter, more cyclic paths reduce oozing and avoid dragging the nozzle over parts that have already been printed, which can make [Z Hop](printer_extruder_z_hop) and [Avoid crossing walls](quality_settings_wall_and_surfaces#avoid-crossing-walls) unnecessary in many plates.

> [!IMPORTANT]
> NEW FEATURE: **Snake and Best of all (shortest path) intra-layer ordering**  
> Available in: [Nightly builds](https://github.com/OrcaSlicer/OrcaSlicer/releases/tag/nightly-builds) or Releases greater than **2.4.2**.

- **Default**: Up to ten instances or islands are visited along the shortest possible closed path. Larger sets use nearest-neighbor chaining, refined by reversing sections of the path (2-opt), moving short runs of stops elsewhere (or-opt) and removing crossings. A good general choice and the recommended option for most plates.
- **As object list**: Instances are printed in the same order as the object list, without any path optimization. Use it when you need a predictable, manually controlled order, for custom sequencing or debugging. [By Object](#by-object) also prints in this order.

    > [!IMPORTANT]
    > NEW FEATURE: **Order By in the plate menu**  
    > Available in: [Nightly builds](https://github.com/OrcaSlicer/OrcaSlicer/releases/tag/nightly-builds) or Releases greater than **2.4.2**.

    To change the order of the object list:

    - Drag an object to a new position inside its plate in the object list.
    - Right-click a plate, in the object list or in the 3D view, and choose **Order By** > **Name**, **Filament**, **Height** or **Size**. **Order By** > **All Plates** sorts the objects of every plate.

    Each sort is ascending. If the objects are already in that order, it reverses them, so choosing the same entry twice gives the descending order. **Name** puts "Part 2" before "Part 10", **Height** compares the top of each object, and **Size** compares the volume of its bounding box. Objects with the same value keep their current order, so an order you made by dragging stays inside each group. Undo restores the previous order.

    > [!TIP]
    >
    > - **Order By** > **Height** prints the tallest object last. With [By Object](#by-object), only the last object can use the full [Printable height](printer_basic_information_printable_space#printable-height). The objects before it must stay below the extruder clearance [Height to lid](printer_basic_information_extruder_clearance#height-to-lid) or [Height to rod](printer_basic_information_extruder_clearance#height-to-rod). An object reported as too tall may slice once it prints last.
    > - **Order By** > **Filament** prints the objects of each filament one after another, which saves filament changes with [By Object](#by-object).

- **Snake**: Serpentine, row-by-row traversal (objects are grouped into rows and each row is traversed in the opposite direction to the previous one), refined with 2-opt. Well suited to regular grids of many small parts.
- **Best of all (shortest path)**: Every strategy is evaluated and the shortest one is used. The object instance order is decided once for the whole print, while the ordering of individual islands is decided per layer, so different layers may end up using different strategies. Slightly slower to slice.

> [!NOTE]
> Except with **As object list**, ordering is applied at the island level, not only per instance, so each separate region of a layer is ordered individually. This mainly benefits assemblies and objects whose layers overlap.
>
> Inside each island, the infill, ironing and support paths are also printed in a short order, whatever this setting: up to eight paths in the shortest possible order, more by refining a nearest-neighbor chain. Paths that must keep their direction, such as [Grid](strength_settings_patterns#grid) infill, are only reordered.
>
> With multiple filaments or tools in the same layer, minimizing tool changes takes priority: objects are grouped by filament first, and this setting only orders the instances within each filament group. The overall sequence may therefore not look like the shortest path across the plate.
