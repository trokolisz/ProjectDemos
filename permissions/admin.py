from django.contrib import admin
from .models import My_User, Permission, UserPermission
# Register your models here.

admin.site.register(My_User)
admin.site.register(Permission)
admin.site.register(UserPermission)