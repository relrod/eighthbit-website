from django.contrib import admin
from bitbin.models import Bit

class BitAdmin(admin.ModelAdmin):
   list_display = ("id","originator","biturl","key","private")

admin.site.register(Bit, BitAdmin)
