更新说明

* 获取新的代码基 https://github.com/dyve/django-bootstrap3

* 复制bootstrap3到当前目录

* 重命名
    BOOSTRSTRAP3 => ZUI；
    bootstrap => zui;
    检查zui3 => zui

* 修改配置(zui.py)

```#!python
...
 'model_renderers': {
        'default': 'scaffold_toolkit.zui.model_renderers.ModelRenderer',
    },
    'model_field_renderers': {
        'default': 'scaffold_toolkit.zui.model_renderers.ModelFieldRenderer'
    },
    ...
```
具体可查阅代码历史记录

增加help_text_as_placeholder设置，且修改renderes.field_renders，以实现此功能