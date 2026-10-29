# support_interface_pattern

> 所在界面：工艺设置 → Support → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_advanced.md` 的「Interface pattern」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Interface pattern

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `support_interface_pattern`.  
[Type](option_type#choice): `Choice`.  
[Options](option_type#choice): `auto, rectilinear, concentric, spiralinset, rectilinear_interlaced, grid`.  
[CLI Example](cli_mode#setting-overrides): `--support-interface-pattern=auto`.  
The pattern used for the support interface.

Each option lays the interface lines out differently, and all of them are measured from [Pattern angle](#pattern-angle), so rotating that rotates the interface with it. The same rules apply to normal and tree supports.

| Option | What you get |
| --- | --- |
| `Default` | Straight lines crossing the support at 90° to Pattern angle. Switches to concentric loops when the interface touches the model, which is the usual case for soluble supports. |
| `Rectilinear` | Straight lines at 90° to Pattern angle. With the [Snug](support_settings_support#snug) style they are rotated a further 45°. |
| `Concentric` | Loops following the outline of the interface, which peel off in one piece and leave no line ends on the surface. |
| `Spiral Inset` | Like `Concentric`, but the loops are joined into a continuous [spiral](strength_settings_patterns#spiral-inset), so the nozzle steps from one ring to the next without stopping. |
| `Rectilinear Interlaced` | Straight lines that swing 45° one way then the other on each successive layer, so the layers cross instead of stacking. This ties the interface together and makes it stiffer under the overhang. |
| `Grid` | Straight lines crossing in a grid on every layer: one set runs along Pattern angle, in line with the [Base Pattern](#base-pattern) below, and the other at 90° to it. |

> [!IMPORTANT]
> NEW FEATURE: **Spiral Inset interface pattern**  
> Available in: [Nightly builds](https://github.com/OrcaSlicer/OrcaSlicer/releases/tag/nightly-builds) or Releases greater than **2.4.2**.

If [Interface spacing](#interface-spacing) is wide enough that the interface is no longer solid, `Default` and `Rectilinear` switch to the base support pattern so that the sparse lines still anchor to each other.
