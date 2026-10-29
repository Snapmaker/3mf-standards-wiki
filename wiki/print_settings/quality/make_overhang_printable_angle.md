# make_overhang_printable_angle

> 所在界面：工艺设置 → Quality → Overhangs
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/quality/quality_settings_overhangs.md` 的「Maximum angle」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

### Maximum angle

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `make_overhang_printable_angle`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--make-overhang-printable-angle=1`.  
Maximum angle of overhangs to allow after making steeper overhangs printable.  
90° will not change the model at all and allow any overhang, while 0 will replace all overhangs with conical material.

![overhang-printable](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/overhangs/overhang-printable.png?raw=true)

> [!TIP]
> Usually, a value between 45° and 60° works well for most printers and models.
