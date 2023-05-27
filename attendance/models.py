from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

from students.models import Students
from branch_class.models import OfficeBranchModel

def validate_date_not_future(date):
    if date > timezone.localdate():
        raise ValidationError("Date cannot be in the future.")

class Attendace(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    date = models.DateField(validators=[validate_date_not_future])
    is_present = models.BooleanField(default=False)
    reason = models.CharField(max_length=200, blank=True)

    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return f"{self.student.student_name} {self.date}"



class Holiday(models.Model):
    branch = models.ForeignKey(OfficeBranchModel,  on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.date} {self.reason}"
    
    class Meta:
        unique_together = ('branch', 'date')

