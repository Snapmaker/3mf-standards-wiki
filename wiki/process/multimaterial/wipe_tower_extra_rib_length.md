# wipe_tower_extra_rib_length

> Location: Process → Multimaterial → Prime tower
> 显隐条件（初步梳理，待校对）：仅非 BBL 机型显示

---

#### Extra rib length

[Mode](../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../developer_reference/built_in_placeholders_variables.md): `wipe_tower_extra_rib_length`.  
[Type](../../general_settings/option_type.md#integer-float-percentage): `Float`.  
[CLI Example](../../cli/cli_mode.md#setting-overrides): `--wipe-tower-extra-rib-length=1`.  
Positive values can increase the size of the rib wall, while negative values can reduce the size. However, the size of the rib wall cannot be smaller than that determined by the purge volume.
