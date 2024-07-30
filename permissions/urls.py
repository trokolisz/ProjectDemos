from django.urls import path
from .views import index, UserPermissionViewSet

urlpatterns = [
    path("", index, name="index"),
    path("api/", UserPermissionViewSet.as_view({'get': 'get_queryset', 'post': 'create', 'put': 'update'}), name="user_permissions_api"),

]