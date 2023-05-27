from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

from django.db.models import Q

from datetime import datetime

from .models import Students
from .serializers import ViewStudentSerializer


from users.permissions import IsAdminUserOrBranchAdminUser
from fee.models import Fees
from branch_class.models import OfficeBranchModel, ClassDivisionModel

class ViewStudents(ListAPIView):
    
    serializer_class = ViewStudentSerializer
    permission_classes = [IsAdminUserOrBranchAdminUser, IsAuthenticated]
    filter_backends = [SearchFilter,]
    search_fields = ['^student_name', 'admission_number', 'phone_number']

    def get_queryset(self):
        queryset = Students.objects.all()

        standard_filter = self.request.query_params.get('standard')
        division_filter = self.request.query_params.get('division')

        if standard_filter and division_filter:
            queryset = queryset.filter(
                Q(student_branch__standard=standard_filter) &
                Q(student_branch__division=division_filter)
            )
        elif standard_filter:
            queryset = queryset.filter(student_branch__standard=standard_filter)
        elif division_filter:
            queryset = queryset.filter(student_branch__division=division_filter)

      
        return queryset




    def get(self, request, branch_id, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.filter(student_branch__branch=branch_id)
        queryset = self.filter_queryset(queryset)
        serializer = ViewStudentSerializer(queryset.order_by('admission_number'), many=True)
        return Response({
            "status":True, 
            "data":serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request, branch_id, *args, **kwargs):
        try:
            branch = OfficeBranchModel.objects.get(id=branch_id)
            class_division = ClassDivisionModel.objects.get(
                standard=request.data.get('standard'),
                division=request.data.get('division'),
                branch=branch
            )
            student = Students.objects.create(
                student_name=request.data.get('student_name').upper(),
                admission_number=request.data.get('admission_number'),
                phone_number=request.data.get('phone_number'),
                student_branch=class_division
            )
            student.save()
            return Response({
                "status":True,
                "message":"Student added successfully"
            }, status=status.HTTP_201_CREATED)
            
        
        except OfficeBranchModel.DoesNotExist:
            return Response({
                "status":False,
                "message":"Branch does not exist"
            }, status=status.HTTP_404_NOT_FOUND)

        except ClassDivisionModel.DoesNotExist:
            return Response({
                "status":False,
                "message":"Class does not exist"
            }, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({
                "status":False,
                "message":str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        

class DashboardOverview(ListAPIView):
    permission_classes = [IsAdminUserOrBranchAdminUser,IsAuthenticated,]

    def get(self, request,branch_id, *args, **kwargs):

        

        total_students = Students.objects.filter(
            student_branch__branch=branch_id
        ).count()
        # total fee paid for this month
        fee_paid = Fees.objects.filter(
            student__student_branch__branch=branch_id
        )
        total_fee_paid = 0
        total_fee = 0
        for fee in fee_paid:
            total_fee += fee.amount
            total_fee_paid += fee.amount_paid
        

        

        total_fee_unpaid = total_fee - total_fee_paid

      

        return Response({
            'status':True,
            'total_students':total_students,
            'total_fee_paid':total_fee_paid,
            'total_fee_unpaid':total_fee_unpaid
        })


