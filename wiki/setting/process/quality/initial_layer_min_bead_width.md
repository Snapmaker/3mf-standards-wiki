# initial_layer_min_bead_width

> Location: Process → Quality → Wall generator
> 本小节同时涵盖：`wall_transition_angle`、`wall_transition_filter_deviation`、`wall_transition_length`、`wall_distribution_count`、`min_bead_width`、`min_feature_size`、`min_length_factor`（各另有独立文档）。

---

## Arachne

The Arachne wall generator dynamically adjusts extrusion width to follow the shape of the model more closely. This allows better handling of thin features and smooth transitions between wall counts.

![wallgenerator-arachne](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/WallGenerator/wallgenerator-arachne.png?raw=true)

> [!NOTE]
> [A Framework for Adaptive Width Control of Dense Contour-Parallel Toolpaths in Fused Deposition Modeling](https://www.sciencedirect.com/science/article/pii/S0010448520301007?via%3Dihub)
