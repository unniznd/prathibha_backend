from django.db import models

class OfficeBranchModel(models.Model):
    branch_name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.branch_name

class ClassDivisionModel(models.Model):
    branch = models.ForeignKey(OfficeBranchModel, on_delete=models.CASCADE)
    standard = models.CharField(max_length=10)
    division = models.CharField(max_length=4)

    class Meta:
        unique_together = ('branch', 'standard', 'division')

    def __str__(self) -> str:
        return f"{self.branch.branch_name} - {self.standard} - {self.division}"

