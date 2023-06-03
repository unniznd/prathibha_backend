from rest_framework import serializers
from students.models import Students
from .models import Attendace, Holiday

class StudentAttendanceSerializer(serializers.ModelSerializer):
    standard = serializers.CharField(source='student_branch.standard')
    division = serializers.CharField(source='student_branch.division')


    class Meta:
        model = Students
        fields = ('admission_number', 'roll_number','student_name', 'standard', 
                  'division','is_absent')
    
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendace
        fields = '__all__'

class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = '__all__'

class StudentAttendanceReportSerializer(serializers.ModelSerializer):
    standard = serializers.CharField(source='student_branch.standard')
    division = serializers.CharField(source='student_branch.division')
    date = serializers.SerializerMethodField()


    class Meta:
        model = Students
        fields = ('admission_number', 'student_name', 'standard', 
                  'division','is_absent')
    
    def get_date(self, obj):
        return self.context.get('date')

class DetailedAttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.student_name')
    phone_number = serializers.CharField(source='student.phone_number')
    class Meta:
        model = Attendace
        fields = ('student_name', 'phone_number' )
       
    