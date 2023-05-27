from django.contrib import admin
from .models import Fees, FeeInstallment

import calendar

@admin.register(Fees)
class FeesAdmin(admin.ModelAdmin):
    list_display = ['name', 'standard','divison','status','amount','amount_paid','branch', 'installment','date_of_payment']

    def name(self, obj):
        return obj.student.student_name
    
    def standard(self, obj):
        return obj.student.student_branch.standard
    
    def divison(self, obj):
        return obj.student.student_branch.division
    
    def branch(self, obj):
        return obj.student.student_branch.branch.branch_name
    
    

@admin.register(FeeInstallment)
class FeeMonthAdmin(admin.ModelAdmin):
    list_display = ['installment', 'is_generated']

    