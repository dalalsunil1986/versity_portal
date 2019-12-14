from django.contrib import admin
from .models import Student

# Register your models here.


class StudentAdmin (admin.ModelAdmin):
    list_display = ['std_id', 'advisor', 'program',
                    'department', 'cgpa', 'is_graduate']
    list_display_links = ['std_id', 'advisor', 'program', 'department', ]
    search_fields = ['std_id', 'advisor', 'program',
                     'department']
    list_filter = ['program', 'department']
    list_per_page = 30


admin.site.register(Student, StudentAdmin)
