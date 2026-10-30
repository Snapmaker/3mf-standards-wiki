# pellet_modded_printer

> Location: Printer → Basic information → Advanced

---

## Pellet Modded Printer

[Mode](../../../general_settings/option_mode.md): `Simple`.  
[Variables](../../../developer_reference/built_in_placeholders_variables.md): `pellet_flow_coefficient`, `pellet_modded_printer`.  
[Type](../../../general_settings/option_type.md): `pellet_flow_coefficient` (Float list), `pellet_modded_printer` (Boolean).  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--pellet-flow-coefficient=1` (`pellet_flow_coefficient` shown; other variables above follow their own type).  
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
