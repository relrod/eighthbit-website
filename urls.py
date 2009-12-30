from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
   (r'^admin/', include(admin.site.urls)),
#   (r'^$', "general.views.front"),
   (r'^wiki/(?P<Title>.*)$', "wiki.views.showpage"),
   (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
   (r'^qdb/quote/(?P<id>.*)$', "qdb.views.showquote"),
   (r'^qdb/addquote/', "qdb.views.addquote"),
   (r'^login/$', login),
   (r'^logout/$', logout),
)
