"""
Configure the models to be displayed in the admin portal.
"""

from django.contrib import admin
from coffee.models.machine import Machine
from coffee.models.pod import Pod

class MachineAdmin(admin.ModelAdmin):
    list_display = ['id','product_type','water_line_compatible','description','code']
admin.site.register(Machine,MachineAdmin)

class PodAdmin(admin.ModelAdmin):
    list_display = ['id','product_type','coffee_flavor','pack_size','description','code']
admin.site.register(Pod,PodAdmin)