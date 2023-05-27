from rest_framework import serializers

from branch_class.models import OfficeBranchModel, ClassDivisionModel

class CreateOfficeBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeBranchModel
        fields = ('branch_name',)

class ViewOfficeBranchSerializer(serializers.ModelSerializer):
    branch_id = serializers.IntegerField(source='id')
    class Meta:
        model = OfficeBranchModel
        fields = ('branch_id', 'branch_name',)

class CreateClassDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDivisionModel
        fields = ('branch', 'standard', 'division')

class ViewClassDivisionSerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(source='branch.branch_name', read_only=True)

    class_division_id = serializers.IntegerField(source='id')

    
    class Meta:
        model = ClassDivisionModel
        fields = ('class_division_id', 'branch_name', 'standard', 'division',)
    
