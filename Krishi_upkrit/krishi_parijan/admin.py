from django.contrib import admin

from .models import MPNTable, MPNRoutingTable

@admin.register(MPNTable)
class MPNTableAdmin(admin.ModelAdmin):
    list_display = ('pk', 'mac', 'available', 'last_active')

@admin.register(MPNRoutingTable)
class MPNRTAdmin(admin.ModelAdmin):
    list_display = ('pk', 'destination', 'distance', 'next_hop')