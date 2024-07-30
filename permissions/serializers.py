from rest_framework import serializers
from .models import Permission, My_User, UserPermission


class UserPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPermission
        fields = ['user', 'permission','len',  'deprecitated', 'days_left', 'got_permission_at']


