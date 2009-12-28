from django.contrib import admin
from eighthbit.wiki.models import Page, Revision
admin.site.register(Page)
admin.site.register(Revision)
