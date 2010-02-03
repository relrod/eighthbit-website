from django.contrib import admin
from qdb.models import *

class QuoteAdmin(admin.ModelAdmin):
   list_display = ("submitter","comment","approved","score")

class VoteAdmin(admin.ModelAdmin):
   list_display = ("quoteid", "txt_direction")

admin.site.register(Quote, QuoteAdmin)
admin.site.register(Vote, VoteAdmin)
