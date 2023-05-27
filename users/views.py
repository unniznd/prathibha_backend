from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Profile, BranchAdmin

from branch_class.models import OfficeBranchModel
from branch_class.serializers import ViewOfficeBranchSerializer


class ObtainAuthTokenWithUserId(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                            context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        profile = Profile.objects.filter(user=user.id).first()
        if(profile.is_admin):
            branches = OfficeBranchModel.objects.all()
            branch_serial = ViewOfficeBranchSerializer(branches, many=True)
            
            return Response({
                'token': token.key, 
                'user_id': user.id,
                'name':profile.name, 
                'is_admin': profile.is_admin,
                'is_branch_admin': profile.is_branch_admin,
                'branches': branch_serial.data

            })
        elif(profile.is_branch_admin):
            branch = BranchAdmin.objects.filter(admin=profile).first().branch
            branch_serial = ViewOfficeBranchSerializer(branch)
            return Response({
                'token': token.key, 
                'user_id': user.id,
                'name':profile.name, 
                'is_admin': profile.is_admin,
                'is_branch_admin': profile.is_branch_admin,
                'branches': branch_serial.data
            })

        return Response({
            'token': token.key, 
            'user_id': user.id,
            'name':profile.name, 
            'is_admin': profile.is_admin,
            'is_branch_admin': profile.is_branch_admin,
        })

class GetDashboardDetails(ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    def get(self, request, *args, **kwargs):
        user = request.user
        profile = Profile.objects.filter(user=user.id).first()
        if(profile.is_admin):
            branches = OfficeBranchModel.objects.all()
            branch_serial = ViewOfficeBranchSerializer(branches, many=True)
            
            return Response({
                'user_id': user.id,
                'name':profile.name, 
                'is_admin': profile.is_admin,
                'is_branch_admin': profile.is_branch_admin,
                'branches': branch_serial.data

            })
        elif(profile.is_branch_admin):
            branch = BranchAdmin.objects.filter(admin=profile).first().branch
            branch_serial = ViewOfficeBranchSerializer(branch)
            return Response({
               
                'user_id': user.id,
                'name':profile.name, 
                'is_admin': profile.is_admin,
                'is_branch_admin': profile.is_branch_admin,
                'branches': branch_serial.data
            })

        return Response({
            'user_id': user.id,
            'name':profile.name, 
            'is_admin': profile.is_admin,
            'is_branch_admin': profile.is_branch_admin,
        })
