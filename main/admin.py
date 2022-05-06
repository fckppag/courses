from django.contrib import admin
from .models import Course, Subcourse


class SubsInLine(admin.TabularInline):
    model = Subcourse
    extra = 3


class CourseAdmin(admin.ModelAdmin):
    fields = ['title']
    inlines = [SubsInLine]


admin.site.register(Course,CourseAdmin)