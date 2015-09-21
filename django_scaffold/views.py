from django_scaffold.forms import UploadTestForm

__author__ = 'YuanXu'
from django.views.generic import FormView


class HomepageView(FormView):
    form_class = UploadTestForm
    template_name = 'home.html'
