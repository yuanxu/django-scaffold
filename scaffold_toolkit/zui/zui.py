# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.importlib import import_module


# Default settings
ZUI_DEFAULTS = {
    'jquery_url': settings.STATIC_URL + "zui/lib/jquery/jquery.js",
    'css_url': None,
    'theme_url': None,
    'javascript_url': None,
    'javascript_in_head': False,
    'include_jquery': False,
    'horizontal_label_class': 'col-md-2',
    'horizontal_field_class': 'col-md-4',
    'set_required': True,
    'set_placeholder': True,
    'required_css_class': '',
    'error_css_class': 'has-error',
    'success_css_class': 'has-success',
    'formset_renderers': {
        'default': 'scaffold_toolkit.zui.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'scaffold_toolkit.zui.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'scaffold_toolkit.zui.renderers.FieldRenderer',
        'inline': 'scaffold_toolkit.zui.renderers.InlineFieldRenderer',
    },
}

# Start with a copy of default settings
ZUI = ZUI_DEFAULTS.copy()

# Override with user settings from settings.py
ZUI.update(getattr(settings, 'ZUI', {}))


def get_zui_setting(setting, default=None):
    """
    Read a setting
    """
    return ZUI.get(setting, default)


def zui_url(postfix):
    """
    Prefix a relative url with the bootstrap base url
    """
    return settings.STATIC_URL + postfix  # get_zui_setting('base_url')


def jquery_url():
    """
    Return the full url to jQuery file to use
    """
    return get_zui_setting('jquery_url')


def javascript_url():
    """
    Return the full url to the Bootstrap JavaScript file
    """
    return get_zui_setting('javascript_url') or \
           zui_url('js/bootstrap.min.js')


def css_url():
    """
    Return the full url to the Bootstrap CSS file
    """
    return get_zui_setting('css_url') or \
           zui_url('css/zui.min.css')


def theme_url():
    """
    Return the full url to the theme CSS file
    """
    return get_zui_setting('theme_url')


def get_renderer(renderers, **kwargs):
    layout = kwargs.get('layout', '')
    path = renderers.get(layout, renderers['default'])
    mod, cls = path.rsplit(".", 1)
    return getattr(import_module(mod), cls)


def get_formset_renderer(**kwargs):
    renderers = get_zui_setting('formset_renderers')
    return get_renderer(renderers, **kwargs)


def get_form_renderer(**kwargs):
    renderers = get_zui_setting('form_renderers')
    return get_renderer(renderers, **kwargs)


def get_field_renderer(**kwargs):
    renderers = get_zui_setting('field_renderers')
    return get_renderer(renderers, **kwargs)
