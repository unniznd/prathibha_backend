from django.db import models
from students.models import Students

from datetime import datetime

STATUS = (
    ('paid', 'Paid'),
    ('unpaid', 'Unpaid'),
)

class FeeInstallment(models.Model):
    year = models.CharField(max_length=20, default=datetime.now().year)
    installment = models.CharField(max_length=20)
    is_generated = models.BooleanField(default=True)

    class Meta:
        unique_together = ['year', 'installment']



    def __str__(self):
        return self.installment

class Fees(models.Model):
    student = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    amount = models.IntegerField()
    amount_paid = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS, default='unpaid')
    installment = models.ForeignKey(FeeInstallment, on_delete=models.DO_NOTHING)
    date_of_payment = models.DateField(auto_now=True)

    class Meta:
        unique_together = ['student', 'installment']

    def __str__(self):
        return self.student.student_name

