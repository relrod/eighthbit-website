from django.contrib import admin
from bitwik.models import *

class PageAdmin(admin.ModelAdmin):
   list_display = ("title", "slug")

admin.site.register(Page, PageAdmin)
admin.site.register(Revision)
