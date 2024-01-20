from django.contrib import admin

from django.contrib import admin
from .models import Section, Student


class SectionAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


admin.site.register(Section, SectionAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "section"]


admin.site.register(Student, StudentAdmin)
