# make_overhang_printable_angle

> Location: Process → Quality → Overhangs

---

### Maximum angle

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `make_overhang_printable_angle`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--make-overhang-printable-angle=1`.  
Maximum angle of overhangs to allow after making steeper overhangs printable.  
90° will not change the model at all and allow any overhang, while 0 will replace all overhangs with conical material.

![overhang-printable](https://github.com/OrcaSlicer/OrcaSlicer_WIKI/blob/main/images/overhangs/overhang-printable.png?raw=true)

> [!TIP]
> Usually, a value between 45° and 60° works well for most printers and models.
