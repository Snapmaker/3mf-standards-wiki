# small_perimeter_threshold

> Location: Process → Speed → Other layers speed

---

### Small perimeters threshold

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `small_perimeter_threshold`.  
[Type](../../../general_settings/option_type.md#list-types): `Float list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--small-perimeter-threshold=1`.  
**Radius** in millimeters below which the speed of perimeters will be reduced to the [small perimeters speed](#small-perimeters).  
A perimeter is considered small when:

$$
\frac{\text{Perimeter Length}}{2\pi} \leq \text{Threshold}
$$

For example, if the threshold is set to 5 mm, then the perimeter length must be less than or equal to 31.4 mm `(2 * π * 5 mm)` to be considered a small perimeter.

- A Circle with a diameter of 10 mm will have a perimeter length of approximately 31.4 mm, which is equal to the threshold, so it will be considered a small perimeter.
- A Cube of 10mm x 10mm will have a perimeter length of 40 mm, which is greater than the threshold, so it will not be considered a small perimeter.
- A Cube of 5mm x 5mm will have a perimeter length of 20 mm, which is less than the threshold, so it will be considered a small perimeter.

> [!NOTE]
> Zero will disable [small perimeters speed](#small-perimeters), and walls will use their regular speed, such as the [outer wall speed](#outer-wall).
