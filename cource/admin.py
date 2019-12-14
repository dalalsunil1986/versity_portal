from django.contrib import admin

from .models import Cource, Section, Classes, CourceLab
# Register your models here.


class CourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'credit',
                    'require_credit', 'department', 'for_all']
    search_fields = ['name', 'short_name']
    list_per_page = 30
    list_filter = ['department', ]


class SectionAdmin(admin.ModelAdmin):
    list_display = ['number', 'cource', 'instructor',
                    'capacity', 'fill', 'taken', 'lab']
    search_fields = ['number', 'cource', 'instructor', ]
    list_per_page = 30


class ClassesAdmin(admin.ModelAdmin):
    list_display = ['section', 'day', 'start',
                    'end', 'duration', 'room_number', 'bulding']
    search_fields = ['section', 'room_number', 'buiding']
    list_filter = ['day', 'bulding']
    list_per_page = 30


class CourceLabAdmin(admin.ModelAdmin):
    list_display = ['section', 'day', 'start',
                    'end', 'duration', 'room_number', 'bulding']
    search_fields = ['section', 'room_number', 'buiding']
    list_filter = ['day', 'bulding']
    list_per_page = 30


admin.site.register(Cource, CourceAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Classes, ClassesAdmin)
admin.site.register(CourceLab, CourceLabAdmin)
