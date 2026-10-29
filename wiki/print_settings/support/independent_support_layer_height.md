# independent_support_layer_height

> 所在界面：工艺设置 → Support → Advanced
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_advanced.md` 的「Independent support layer height」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Independent support layer height

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `independent_support_layer_height`.  
[Type](option_type#boolean): `Boolean`.  
[CLI Example](cli_mode#setting-overrides): `--independent-support-layer-height=1`.  
Support layers use a layer height independent of the object layers. This allows a custom Z gap and saves print time. This option is ignored when a prime tower is printed, and it is not available with the Organic tree support style.

Turning this on changes the height of the support layers, not their number: you still get exactly the [Interface layers](#interface-layers) you asked for, including with the `Tree Slim`, `Tree Strong` and `Tree Hybrid` styles.
