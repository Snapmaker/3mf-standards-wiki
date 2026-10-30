# spiral_mode_smooth

> Location: Process → Others → Special mode

---

### Smooth Spiral

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `spiral_mode_smooth`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--spiral-mode-smooth=1`.  
When enabled, Smooth Spiral smooths out X and Y moves as well, resulting in no visible seams even on non-vertical walls.  
This produces the smoothest possible spiral print.

> [!NOTE]
> If you are using absolute E distances, the smoothing may not work as expected.
