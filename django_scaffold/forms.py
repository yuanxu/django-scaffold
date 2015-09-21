# coding='utf-8'
from scaffold_toolkit.forms import KindEditor

__author__ = 'YuanXu'
from django import forms


class UploadTestForm(forms.Form):
    content = forms.CharField(widget=KindEditor)
