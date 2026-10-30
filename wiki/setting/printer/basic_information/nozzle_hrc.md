# nozzle_hrc

> Location: Printer → Basic information → Accessory

---

## Nozzle HRC

[Mode](../../../general_settings/option_mode.md): `Developer`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `nozzle_hrc`.  
[Type](../../../general_settings/option_type.md#integer-float-percentage): `Integer`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--nozzle-hrc=1`.  
The Nozzle Hardness ([Hardness Rockwell C](https://en.wikipedia.org/wiki/Rockwell_hardness_test)) value is used in OrcaSlicer to validate nozzle compatibility with abrasive filaments and prevent nozzle damage during printing.

| Material          | Value |
|-------------------|-------|
| Disable Check     | 0     |
| Brass             | 2     |
| Stainless Steel   | 20    |
| Hardened Steel    | 55    |
| Tungsten Carbide  | 85    |
