from rest_framework import serializers
from .models import AdminFacing,Task

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdminFacing 
        fields=['app_name','link','points','category','sub_category']

class AdminUserFacingSerializer(serializers.ModelSerializer):
        class Meta:
            model=AdminFacing 
            fields=['app_name','link','points','category','sub_category']
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=['admin_data','image_proof']
