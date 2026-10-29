# nozzle_hrc

> 所在界面：打印机设置 → Basic information → Accessory
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/basic information/printer_basic_information_accessory.md` 的「Nozzle HRC」小节（2026-10-28），英文原文，待本地化校对。

---

## Nozzle HRC

[Mode](option_mode): `Developer`.  
[Variable](built_in_placeholders_variables): `nozzle_hrc`.  
[Type](option_type#integer-float-percentage): `Integer`.  
[CLI Example](cli_mode#setting-overrides): `--nozzle-hrc=1`.  
The Nozzle Hardness ([Hardness Rockwell C](https://en.wikipedia.org/wiki/Rockwell_hardness_test)) value is used in OrcaSlicer to validate nozzle compatibility with abrasive filaments and prevent nozzle damage during printing.

| Material          | Value |
|-------------------|-------|
| Disable Check     | 0     |
| Brass             | 2     |
| Stainless Steel   | 20    |
| Hardened Steel    | 55    |
| Tungsten Carbide  | 85    |
