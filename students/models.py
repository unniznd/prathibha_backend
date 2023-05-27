from django.db import models

from branch_class.models import ClassDivisionModel

class Students(models.Model):
    admission_number = models.IntegerField(unique=True, primary_key=True)
    student_name = models.CharField(max_length=200)
    student_branch = models.ForeignKey(ClassDivisionModel, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    is_absent = models.BooleanField(default=False)

    def __str__(self):
        return self.student_name
    
