from django.contrib import admin
from qdb.models import *

class QuoteAdmin(admin.ModelAdmin):
   list_display = ("submitter","comment","approved","score")

admin.site.register(Quote, QuoteAdmin)
