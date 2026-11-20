# dithering_local_z_infill

> Location: Process → Multimaterial → Color Mixing (Experimental) → Apply subdivision to infill
> Status: placeholder — fork-specific parameter, to be completed.

---

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `dithering_local_z_infill`.  
[Type](../../../general_settings/option_type.md#boolean): `Boolean`.  
[Default](../../../general_settings/option_type.md#default-value): `false`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--dithering-local-z-infill=1`.  

Experimental. When Subdivide Mix Layer is enabled, also apply the same subdivision to infill inside mixed-color areas.\n\nThis is enabled automatically with Subdivide Mix Layer. Turn it off to keep infill on the normal layer height.\n\nIt can improve internal color mixing, but may add toolchanges and affect infill behavior.
