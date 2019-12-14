from django.contrib import admin
from .models import Teacher

# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'teacher_id', 'program', 'available']
    search_fields = ['first_name', 'last_name', 'teacher_id', ]
    list_filter = ['program', ]
    list_per_page = 30


admin.site.register(Teacher, TeacherAdmin)
