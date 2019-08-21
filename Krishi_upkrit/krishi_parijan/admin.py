from django.contrib import admin

from .models import MPN

@admin.register(MPN)
class MPNAdmin(admin.ModelAdmin):
    list_display = ('pk', 'mac', 'available', 'last_active')