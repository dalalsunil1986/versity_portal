from django.contrib import admin
from .models import Semester

# Register your models here.


class SemesterAdmin(admin.ModelAdmin):
    list_display = ['title', 'season', 'year']
    search_fields = ['title', 'season', 'year']
    list_per_page = 30


admin.site.register(Semester, SemesterAdmin)
