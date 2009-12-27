from django.contrib import admin
from roadmap.models import *

class StopsignAdmin(admin.ModelAdmin):
   list_display = ("project","what","percent","status",)

admin.site.register(Project)
admin.site.register(Version)
admin.site.register(Stopsign, StopsignAdmin)
