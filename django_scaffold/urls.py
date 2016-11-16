from django.conf.urls import  url
# from django.contrib import admin
from django_scaffold.views import HomepageView
from scaffold_toolkit.views import kindeditor_upload_file

urlpatterns = [
    # Examples:
    url(r'^$', HomepageView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^uplaod/$', kindeditor_upload_file, name='kind_upload')
]
