from django.contrib import admin
from .models import Attendace, Holiday

@admin.register(Attendace)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'is_present', 'reason')
    list_filter = ('student', 'date', 'is_present')
    search_fields = ('student__student_name', 'date', 'is_present')

@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ('branch_name','date', 'reason')
    list_filter = ('date', 'reason')
    search_fields = ('date', 'reason')

    def branch_name(self, obj):
        return obj.branch.branch_name
