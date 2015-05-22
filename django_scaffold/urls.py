from django.conf.urls import patterns, include, url
# from django.contrib import admin
from scaffold_toolkit.views import kindeditor_upload_file

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'django_scaffold.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^uplaod/$', kindeditor_upload_file, name='kind_upload')
                       )
