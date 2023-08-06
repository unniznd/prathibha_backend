from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse

from users.permissions import IsAdminUserOrBranchAdminUser

from attendance.models import Attendace   
from attendance.serializers import StudentAttendanceReportSerializer
from students.models import Students
from fee.models import Fees

from datetime import timedelta
from datetime import datetime


import csv

class AttendanceReport(ListAPIView):
    serializer_class = StudentAttendanceReportSerializer
    permission_classes = [IsAdminUserOrBranchAdminUser, IsAuthenticated]
        

    def get(self, request, branchId, *args, **kwargs):
        queryset = Students.objects.all()
        from_date = datetime.strptime(self.request.query_params.get('from', None),'%Y-%m-%d')
        to_date = datetime.strptime(self.request.query_params.get('to', None),'%Y-%m-%d')
        view = self.request.query_params.get('view', None)

        if not from_date or not to_date:
            return Response({
                "message": "Please provide from and to date"
            }, status=status.HTTP_400_BAD_REQUEST)

        if from_date>to_date:
            return Response({
                "message": "From date cannot be greater than to date"
            }, status=status.HTTP_400_BAD_REQUEST)

        if view == "csv" :
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="attendace_reports_{from_date} - {to_date}.csv"'

            # Create the CSV writer
            writer = csv.writer(response)

            # Write the header row
            writer.writerow(['Admission Number', 'Student Name', 'Standard', 'Division', 'Date', 'Status'])

          
            while from_date<=to_date:
                for student in queryset:
                    writer.writerow([
                        student.admission_number,
                        student.student_name,
                        student.student_branch.standard,
                        student.student_branch.division,
                        datetime.strftime(from_date, "%B %d, %Y"),
                        "Present" if Attendace.objects.filter(student=student.admission_number, date=from_date).first() else "Absent"
                    ])
                   

                from_date = from_date + timedelta(days=1)

            return response

        reports = []
    

        while from_date<=to_date:
            for student in queryset:
                report = {}
                report["admission_number"] = student.admission_number
                report["student_name"] = student.student_name
                report["standard"] = student.student_branch.standard
                report["division"] = student.student_branch.division
                report["date"] = datetime.strftime(from_date, "%B %d, %Y")
                report["status"] = "Present"
                attendance = Attendace.objects.filter(student=student.admission_number, date=from_date).first()
                if attendance:
                    report["status"] = "Absent"
                
                reports.append(report)     

            from_date = from_date + timedelta(days=1)

        
        return Response({"status":True, "data":reports}, status=status.HTTP_200_OK)


class FeeReport(ListAPIView):
    permission_classes = [IsAdminUserOrBranchAdminUser, IsAuthenticated]
        

    def get(self, request, branchId, *args, **kwargs):
        # get from month, to month and view as parameters from query params
        # filter fee objects based on the above params

        from_date = datetime.strptime(self.request.query_params.get('from', None),'%Y-%m-%d')
        to_date = datetime.strptime(self.request.query_params.get('to', None),'%Y-%m-%d')
        view = self.request.query_params.get('view', None)

        if not from_date or not to_date:
            return Response({
                "message": "Please provide from and to date"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if from_date>to_date:
            return Response({
                "message": "From date cannot be greater than to date"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if view == "csv" :
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="fee_reports_{from_date} - {to_date}.csv"'

            # Create the CSV writer
            writer = csv.writer(response)

            # Write the header row
            writer.writerow(['Admission Number', 'Student Name', 'Standard', 
                             'Division', 'Date', 'Status', 'Installment'])

            queryset = Fees.objects.filter(date_of_payment__gte=from_date, date_of_payment__lte=to_date)

            for fee in queryset:
                writer.writerow([
                    fee.student.admission_number,
                    fee.student.student_name,
                    fee.student.student_branch.standard,
                    fee.student.student_branch.division,
                    datetime.strftime(fee.date_of_payment, "%B %d, %Y"),
                    fee.status,
                    fee.installment.installment
                ])

            return response
        
        queryset = Fees.objects.filter(date_of_payment__gte=from_date, date_of_payment__lte=to_date)
        reports = []

        for fee in queryset:
            report = {}
            report["admission_number"] = fee.student.admission_number
            report["student_name"] = fee.student.student_name
            report["standard"] = fee.student.student_branch.standard
            report["division"] = fee.student.student_branch.division
            report["date"] = datetime.strftime(fee.date_of_payment, "%B %d, %Y")
            report["status"] = fee.status.capitalize()
            report["installment"] = fee.installment.installment
            reports.append(report)

        return Response({
            "status":True,
            "data":reports
        }, status=status.HTTP_200_OK)