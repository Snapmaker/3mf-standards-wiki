# support_interface_pattern

> Location: Process → Support → Advanced

---

## Interface pattern

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `support_interface_pattern`.  
[Type](../../general_settings/option_type.md#choice): `Choice`.  
[Options](../../general_settings/option_type.md#choice): `auto, rectilinear, concentric, spiralinset, rectilinear_interlaced, grid`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--support-interface-pattern=auto`.  
The pattern used for the support interface.

Each option lays the interface lines out differently, and all of them are measured from [Pattern angle](#pattern-angle), so rotating that rotates the interface with it. The same rules apply to normal and tree supports.

| Option | What you get |
| --- | --- |
| `Default` | Straight lines crossing the support at 90° to Pattern angle. Switches to concentric loops when the interface touches the model, which is the usual case for soluble supports. |
| `Rectilinear` | Straight lines at 90° to Pattern angle. With the [Snug](../../process/support/support_settings_support.md#snug) style they are rotated a further 45°. |
| `Concentric` | Loops following the outline of the interface, which peel off in one piece and leave no line ends on the surface. |
| `Spiral Inset` | Like `Concentric`, but the loops are joined into a continuous [spiral](../../process/strength/strength_settings_patterns.md#spiral-inset), so the nozzle steps from one ring to the next without stopping. |
| `Rectilinear Interlaced` | Straight lines that swing 45° one way then the other on each successive layer, so the layers cross instead of stacking. This ties the interface together and makes it stiffer under the overhang. |
| `Grid` | Straight lines crossing in a grid on every layer: one set runs along Pattern angle, in line with the [Base Pattern](#base-pattern) below, and the other at 90° to it. |

> [!IMPORTANT]
> NEW FEATURE: **Spiral Inset interface pattern**  
> Available in: [Nightly builds](https://github.com/OrcaSlicer/OrcaSlicer/releases/tag/nightly-builds) or Releases greater than **2.4.2**.

If [Interface spacing](#interface-spacing) is wide enough that the interface is no longer solid, `Default` and `Rectilinear` switch to the base support pattern so that the sparse lines still anchor to each other.
