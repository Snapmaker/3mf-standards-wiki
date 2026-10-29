# notes

> 所在界面：工艺设置 → Others → Notes
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_notes.md` 的「Notes」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

# Notes

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `notes`.  
[Type](option_type#text): `Text`.  
[CLI Example](cli_mode#setting-overrides): `--notes=value`.  
You can put your notes regarding this process profile here.  
They are added as a comment to the configuration block of the G-code.

```gcode
; notes = Sliced with OrcaSlicer, the best slicer.
```
