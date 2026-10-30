# max_travel_detour_distance

> Location: Process → Quality → Walls and surfaces

---

### Max detour length

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `max_travel_detour_distance`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Float or Percentage`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--max-travel-detour-distance=20%`.  
Defines the maximum distance the printer is allowed to detour to avoid crossing a wall.
Can be set as:

- **Absolute value in millimeters:** exactly how far the detour can extend (e.g., `5mm`).
- **Percentage** of the direct travel path (e.g., `50%`).
- **0** disables the **limit** and allows detours of **any length**.

Use this setting to balance print time and wall quality: longer detours mean fewer wall crossings but slower prints.
