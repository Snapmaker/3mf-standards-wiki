# raft_first_layer_expansion

> 所在界面：工艺设置 → Support → Support
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/support/support_settings_support.md` 的「Initial layer expansion」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

## Initial layer expansion

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `raft_first_layer_expansion`.  
[Type](option_type#integer-float-percentage): `Float`.  
[CLI Example](cli_mode#setting-overrides): `--raft-first-layer-expansion=1`.  
Expands the first raft or support layer to improve build plate adhesion. It is disabled for the Tree Slim and Tree Strong styles unless a raft is used.
