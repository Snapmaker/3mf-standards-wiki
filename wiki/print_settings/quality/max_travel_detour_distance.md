# max_travel_detour_distance

> 所在界面：工艺设置 → Quality → Walls and surfaces
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_wall_and_surfaces.md` 的「Max detour length」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Max detour length

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `max_travel_detour_distance`.  
[Type](option_type#integer-float-percentage): `Float or Percentage`.  
[CLI Example](cli_mode#setting-overrides): `--max-travel-detour-distance=20%`.  
Defines the maximum distance the printer is allowed to detour to avoid crossing a wall.
Can be set as:

- **Absolute value in millimeters:** exactly how far the detour can extend (e.g., `5mm`).
- **Percentage** of the direct travel path (e.g., `50%`).
- **0** disables the **limit** and allows detours of **any length**.

Use this setting to balance print time and wall quality: longer detours mean fewer wall crossings but slower prints.
