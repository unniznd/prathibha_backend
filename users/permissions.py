from rest_framework.permissions import BasePermission

from users.models import Profile

class IsAdminUserOrBranchAdminUser(BasePermission):
    def has_permission(self, request, view):
        profile = Profile.objects.filter(user=request.user).first()
        if not profile:
            return False
        
        if profile.is_admin or profile.is_branch_admin:
            return True

        return False

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        profile = Profile.objects.filter(user=request.user).first()
        if not profile:
            return False
        
        if profile.is_admin:
            return True

        return False

class IsBranchAdminUser(BasePermission):
    def has_permission(self, request, view):
        profile = Profile.objects.filter(user=request.user).first()
        if not profile:
            return False
        
        if profile.is_branch_admin:
            return True

        return False
