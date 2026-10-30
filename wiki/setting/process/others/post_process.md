# post_process

> Location: Process → Others → Post-processing Scripts

---

# Post-Processing Scripts

[Mode](../../../general_settings/option_mode.md): `Advanced`.  
[Variable](../../../developer_reference/built_in_placeholders_variables.md): `post_process`.  
[Type](../../../general_settings/option_type.md#list-types): `Text list`.  
[CLI Example](../../../cli/cli_mode.md#setting-overrides): `--post-process=value`.  
Here you can set up post-processing scripts that run on the generated G-code.  
For Bambu Lab printers, they run right after slicing, so the preview shows the processed G-code. For other printers, they run only when a G-code file is exported or sent to a network printer with **Print** or **Send**, so the preview and sliced 3MF files keep the unprocessed G-code.  
This allows you to modify the G-code output or perform additional tasks.

Check the script's documentation for dependencies, available parameters and usage instructions.

Example Python script:

```pwsh
"C:\Your\Path\To\Python\python.exe" "C:\Your\Path\To\Script\pythonScript.py" -parameterToScript 1994;
```
