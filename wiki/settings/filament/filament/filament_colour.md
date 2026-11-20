# filament_colour

> Location: Filament → Filament → Basic information
> Status: placeholder — to be completed.
> Note: this key is not rendered inside the filament tab; it is edited via the color swatch of the filament list in the left panel of the prepare view (see below).

## Basic information

- Label: Color
- Mode: Advanced
- Type: Text list (color picker; one `#RRGGBB` color string per slot)
- Default: #F2754E

> Tooltip: Only used as a visual help on UI.

## Where to edit

The actual entry points:

- **The filament list in the left panel of the prepare view** — one row per filament slot; the color swatch at the start of each row is this key. Clicking it opens the color picker (with color-library and dual/gradient multi-color support; falls back to the system color picker when no color-library entry matches).
- Changes are written to `filament_colour[slot]` in `project_config`, i.e. they take effect **per project, per slot**, not as a filament preset parameter.

## Purpose and relations

- Purely a UI visual aid: the 3D preview renders each slot's model color from it; it does not affect slicing.
- Saved into the 3mf with the project and written per slot as a gcode comment: `; filament_colour = #F4E2C1;#00C1AE;...` (listed in table 1 of the Feishu "gcode field interaction protocol").
- Difference from [`default_filament_colour`](default_filament_colour.md): the latter is the preset's default color (Basic information section); this key is the color actually in effect per slot in the current project, initialized from the preset value when loading.
- Color-mixing system: `filament_colour` is the slot's "physical color"; `filament_multi_colors`/`filament_colour_mode` (Snapmaker V2.3.5 extension) describe the dual/gradient display colors.

(To add: AMS slot syncing, color-library matching rules)
