from django.contrib import admin

from users.models import Profile, BranchAdmin

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'is_admin', 'is_branch_admin')

    def user(self, obj):
        return obj.user.username
    

@admin.register(BranchAdmin)
class BranchAdminAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch')

    def name(self, obj):
        return obj.admin.name