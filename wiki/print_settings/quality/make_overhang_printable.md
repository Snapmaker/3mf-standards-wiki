# make_overhang_printable

> 所在界面：工艺设置 → Quality → Overhangs
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_overhangs.md` 的「Make overhang printable」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Make overhang printable

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `make_overhang_printable`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--make-overhang-printable=1`.  
This setting will modify the geometry to print overhangs without support material.  
Every overhang exceeding the [maximum angle](#maximum-angle) will be modified to be printable.
