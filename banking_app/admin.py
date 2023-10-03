# admin.py

from django.contrib import admin
from .models import District, Branch

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class BranchAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'district']

admin.site.register(District, DistrictAdmin)
admin.site.register(Branch, BranchAdmin)
