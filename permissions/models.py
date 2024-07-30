from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
import django.utils.timezone as timezone

# Create your models here.
class My_User(models.Model):
    name = models.CharField(max_length=100, null=False)
    tsz = models.IntegerField(null=False, default=0, validators=[MinValueValidator(100000), MaxValueValidator(999999)], unique=True)
    # created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self)->str:
        return f"{self.name} - {self.tsz}"
    
    def student(self)->bool:
        if self.tsz  >= 16000 and self.tsz <17000:
            return True        
        return False
    

class Permission(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    len = models.IntegerField(default=200)

    def __str__(self) -> str:
        return self.name + " - " + self.len.__str__()
    
    
    
   
    

class UserPermission(models.Model):
    user = models.ForeignKey(My_User, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    got_permission_at = models.DateField()

    class Meta:
        unique_together = ('user', 'permission')

    def days_since_updated(self) -> int:
        today = timezone.now()
    
        today = datetime.date(today.year, today.month, today.day)
        got_perms_at = datetime.date(self.got_permission_at.year, self.got_permission_at.month, self.got_permission_at.day)

        delta = today - got_perms_at
        return delta.days
    
    def deprecitated(self) -> bool:
        return self.days_since_updated() > self.permission.len
    
    def __str__(self) -> str:
        if self.deprecitated():
            return f"Deprecitated {self.user.name} - {self.permission.name} - {self.days_since_updated()} days ago"            
        return f"{self.user.name} - {self.permission.name} - {self.days_since_updated()} days ago"
    
    def days_left(self) -> int:
        return self.permission.len - self.days_since_updated()
    
    def len(self) ->int:
        return self.permission.len
    
    def reset(self) ->bool:
        self.got_permission_at = timezone.now()
        self.save()
        return True