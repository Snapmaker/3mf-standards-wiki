# small_perimeter_speed

> Location: Process → Speed → Other layers speed

---

## Small perimeters

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `small_perimeter_speed`.  
[Type](../../../general_settings/option_type.md#list-types): `Float or Percentage list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--small-perimeter-speed=20%`.  
Speed of walls with a theoretical radius <= [small perimeters threshold](#small-perimeters-threshold).
Any shape (not only circles) will be considered as a small perimeter.

If expressed as a percentage (for example: 80%), it will be calculated on the [outer wall speed](#outer-wall).

> [!NOTE]
> The default is 50% of the [outer wall speed](#outer-wall).
