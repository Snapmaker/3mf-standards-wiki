# post_process

> 所在界面：工艺设置 → Others → Post-processing Scripts
> 来源：拷贝自上游 OrcaSlicer wiki `print_settings/others/others_settings_post_processing_scripts.md` 的「Post-Processing Scripts」小节（2026-10-28，上游 commit ff45e25），英文原文，待本地化校对。

---

# Post-Processing Scripts

[Mode](option_mode): `Advanced`.  
[Variable](built_in_placeholders_variables): `post_process`.  
[Type](option_type#list-types): `Text list`.  
[CLI Example](cli_mode#setting-overrides): `--post-process=value`.  
Here you can set up post-processing scripts that run on the generated G-code.  
For Bambu Lab printers, they run right after slicing, so the preview shows the processed G-code. For other printers, they run only when a G-code file is exported or sent to a network printer with **Print** or **Send**, so the preview and sliced 3MF files keep the unprocessed G-code.  
This allows you to modify the G-code output or perform additional tasks.

Check the script's documentation for dependencies, available parameters and usage instructions.

Example Python script:

```pwsh
"C:\Your\Path\To\Python\python.exe" "C:\Your\Path\To\Script\pythonScript.py" -parameterToScript 1994;
```
