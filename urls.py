from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
   (r'^admin/', include(admin.site.urls)),
   (r'^$', "general.views.front"),
   (r'^wiki/(?P<page>.*)$', "wiki.views.showpage"),
   (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
   (r'^login/$', login),
   (r'^logout/$', logout),
)
