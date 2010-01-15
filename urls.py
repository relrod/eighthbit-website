from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',

   # Core Site:
   (r'^admin/', include(admin.site.urls)),

   # This should be removed for production.
   (r'^media/(?P<path>.*)/$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

   # BitWik:
   (r'^wiki/(?P<title>.*)/edit/$', "bitwik.views.edit"),
   (r'^wiki/(?P<title>.*)/$', "bitwik.views.showpage"),

   # BitBin
   (r'^bitbin/(?P<id>.+)/$', "bitbin.views.paste"),

      
   # QDB:
   (r'^qdb/quote/(?P<id>[0-9]+)/(?P<direction>up|down)/$', "qdb.views.vote"),
   (r'^qdb/quote/(?P<id>.*)/$', "qdb.views.showquote"),
   (r'^qdb/random/$', "qdb.views.showquote", {"id": "random"}),
   (r'^qdb/add/$', "qdb.views.addquote"),
   (r'^qdb/addquote/$', "qdb.views.addquote"),
   (r'^qdb/list/(?P<page>\d+)/$', "qdb.views.list"),
   (r'^qdb/$', "qdb.views.list", {"page" : 1} ),

   # Authentication
   (r'^login/$', login),
   (r'^logout/$', logout),
)
