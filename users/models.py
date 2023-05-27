from django.db import models
from django.contrib.auth.models import User

from branch_class.models import OfficeBranchModel

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    is_admin = models.BooleanField(default=False)
    is_branch_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class BranchAdmin(models.Model):
    admin = models.OneToOneField(Profile, on_delete=models.CASCADE)
    branch = models.ForeignKey(OfficeBranchModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.admin.name + " - " + self.branch.branch_name
