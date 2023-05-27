from rest_framework import serializers
from .models import Fees
import inflect

class FeeSerializer(serializers.ModelSerializer):
    fee_id = serializers.IntegerField(source='id')
    admission_number = serializers.CharField(source='student.admission_number')
    student_name = serializers.CharField(source='student.student_name')
    standard = serializers.CharField(source='student.student_branch.standard')
    division = serializers.CharField(source='student.student_branch.division')
    branch = serializers.CharField(source='student.student_branch.branch.branch_name')
    status = serializers.CharField(source='get_status_display')
    date_of_payment = serializers.SerializerMethodField()
    amount_left = serializers.SerializerMethodField()
    installment = serializers.SerializerMethodField()

    class Meta:
        model = Fees
        fields = ['fee_id' , 'admission_number','student_name', 'standard', 'division', 'branch', 
                  'amount', 'amount_left','status', 'installment','date_of_payment']
        

    def get_date_of_payment(self, obj):
        return obj.date_of_payment.strftime("%B %d, %Y")
    
    def get_amount_left(self, obj):
        return obj.amount - obj.amount_paid

    def get_installment(self, obj):
        p = inflect.engine()
        return p.ordinal(int(obj.installment.installment))