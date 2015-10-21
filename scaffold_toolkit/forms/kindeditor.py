# coding=utf-8
from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from django.forms import Textarea
from django.utils.safestring import mark_safe

editorBasePath = '%s%s' % (settings.STATIC_URL, 'zui/lib/kindeditor/')


class KindEditor(Textarea):
    scheme = 'default'
    toolbar = 'mini'

    def __init__(self, attrs=None):
        attrs = attrs or {}
        attrs['rel'] = 'kind'
        if attrs and 'toolbar' in attrs:
            self.toolbar = attrs['toolbar']
        super(KindEditor, self).__init__(attrs)

    def _media(self):
        use_require = getattr("settings", "KINDEDITOR_USE_REQUERYJS", False)
        if use_require:
            return forms.Media(css={'all': ('%sthemes/default/default.css' % editorBasePath,)})
        else:
            return forms.Media(css={'all': ('%sthemes/default/default.css' % editorBasePath,)},
                               js=('%skindeditor.min.js' % editorBasePath,))

    media = property(_media)

    def _get_toolbar_items(self):
        if self.toolbar == 'mini':
            return """
            ,items : ['fontname', 'fontsize', '|', 'forecolor', 'hilitecolor', 'bold', 'italic', 'underline',
            'removeformat', '|', 'justifyleft', 'justifycenter', 'justifyright', 'insertorderedlist',
            'insertunorderedlist', '|', 'emoticons', 'image', 'link']
            """
        elif self.toolbar == 'small':
            return """
            ,items : ['bold', 'italic', 'underline', 'strikethrough', 'removeformat','|','insertorderedlist', 'insertunorderedlist',
                   'forecolor', 'hilitecolor', 'fontname', 'fontsize','subscript','superscript',  '|', 'link', 'unlink', 'emoticons',
                   'shcode', 'image', 'flash', 'quote', '|','about']"""
        else:
            return """,items: %s""" % self.toolbar

    def _get_kind_attrs(self):
        return ''.join((
            ',width:"%s"' % (self.attrs['width'] if 'width' in self.attrs else '100%'),
            ',height:%s' % self.attrs['height'] if 'height' in self.attrs else '',
            self._get_toolbar_items()
        ))

    def render(self, name, value, attrs=None):
        use_require = getattr("settings", "KINDEDITOR_USE_REQUERYJS", False)
        if use_require:
            js_staff = '''<script type="text/javascript">
            require(["kindeditor"],function(){ %s });
            </script>
            '''
        else:
            js_staff = '''<script type="text/javascript">
            %s
            </script>
            '''
        js = u'''
                 KindEditor.lang('zh_CN');
                var editor_%s;
                KindEditor.ready(function(K) {
                    editor_%s = K.create('#%s',
                    {themeType:'%s'%s,
                    filterMode:false,
                    uploadJson:'%s',
                    });
                });
        ''' % (name, name, 'id_' + name, self.scheme,
               self._get_kind_attrs(), reverse('kind_upload'))
        js = js_staff % js
        textarea = super(KindEditor, self).render(name, value, attrs)
        textarea += js
        return mark_safe(textarea)
