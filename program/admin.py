from django.contrib import admin
from .models import Program, Department

# Register your models here.


class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name']
    search_fields = ['name', 'short_name']
    list_per_page = 30


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name']
    search_fields = ['name', 'short_name']
    list_per_page = 30


admin.site.register(Program, ProgramAdmin)
admin.site.register(Department, DepartmentAdmin)
