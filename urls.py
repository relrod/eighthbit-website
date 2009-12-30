from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',

   # Core Site:
   (r'^admin/', include(admin.site.urls)),
   (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

   # Wiki:
   #(r'^wiki/(?P<Title>.*)$', "wiki.views.showpage"),
   
   # QDB:
   (r'^qdb/quote/(?P<id>.*)$', "qdb.views.showquote"),
   (r'^qdb/random/$', "qdb.views.showquote", {"id": "random"}),
   (r'^qdb/add/$', "qdb.views.addquote"),
   (r'^qdb/addquote/$', "qdb.views.addquote"),
   (r'^qdb/list/(?P<page>\d+)$', "qdb.views.list"),

   # Authentication
   (r'^login/$', login),
   (r'^logout/$', logout),
)
