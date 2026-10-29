# pellet_modded_printer

> 所在界面：打印机设置 → Basic information → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `printer_settings/basic information/printer_basic_information_advanced.md` 的「Pellet Modded Printer」小节（2026-10-28），英文原文，待本地化校对。

---

## Pellet Modded Printer

[Mode](option_mode): `Simple`.  
[Variables](built_in_placeholders_variables): `pellet_flow_coefficient`, `pellet_modded_printer`.  
[Type](option_type): `pellet_flow_coefficient` (Float list), `pellet_modded_printer` (Boolean).  
[CLI Example](cli_mode#setting-overrides): `--pellet-flow-coefficient=1` (`pellet_flow_coefficient` shown; other variables above follow their own type).  
Enable this option if your printer uses pellets instead of filaments.
Large format printers with print volumes in the order of 1m^3 generally use pellets for printing.
The overall tech is very similar to FDM printing.
It is FDM printing, but instead of filaments, it uses pellets.

The difference here is that where filaments have a filament_diameter that is used to calculate the volume of filament ingested, pellets have a particular flow_coefficient that is empirically devised for that particular pellet.

pellet_flow_coefficient is basically a measure of the packing density of a particular pellet.
Shape, material and density of an individual pellet will determine the packing density and the only thing that matters for 3d printing is how much of that pellet material is extruded by one turn of whatever feeding mehcanism/gear your printer uses. You can emperically derive that for your own pellets for a particular printer model.

We are translating the pellet_flow_coefficient into filament_diameter so that everything works just like it does already with very minor adjustments.

$$
\text{filament\_diameter} = \sqrt{\frac{4}{\text{pellet\_flow\_coefficient} \cdot \pi}}
$$

sqrt just makes the relationship between flow_coefficient and volume linear.

Higher packing density -> more material extruded by single turn -> higher pellet_flow_coefficient -> treated as if a filament of larger diameter is being used. All other calculations remain the same for slicing.
