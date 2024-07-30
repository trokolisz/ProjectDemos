from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, renderers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserPermissionSerializer
from .models import Permission, My_User, UserPermission
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'index.html')

class UserPermissionViewSet(viewsets.ViewSet):
    queryset = UserPermission.objects.all()
    serializer_class = UserPermissionSerializer
    #renderer_classes = [renderers.JSONRenderer]
    
    def get_queryset(self, request):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({"error": "user_id is required"}, status=400)
        try:
            user = My_User.objects.get(id=user_id)
        except My_User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        
        user_permissions = UserPermission.objects.filter(user=user)
        serializer = UserPermissionSerializer(user_permissions, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = UserPermissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request):
        request_data = request.data
        print(request_data)
        user_id = request_data.get('user')
        permission_id = request_data.get('permission')
        if not user_id:
            return Response({"error": "user is required"}, status=400)
        if not permission_id:
            return Response({"error": "permission is required"}, status=400)

        try:
            user = My_User.objects.get(id=user_id)
        except My_User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        
        try:
            permission = Permission.objects.get(id=permission_id)
        except Permission.DoesNotExist:
            return Response({"error": "Permission not found"}, status=404)
        
        user_permission = UserPermission.objects.filter(user=user, permission=permission).first()
        if not user_permission:
            return Response({"error": "User permission not found"}, status=404)
        
        user_permission.got_permission_at = timezone.now()
        user_permission.save()
        
        return Response(status=status.HTTP_200_OK)
    

