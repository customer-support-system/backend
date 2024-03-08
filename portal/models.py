from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,Permission,Group
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from portal import constants




class CustomUserManager(BaseUserManager):
   
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Users must have is_staff=True.')
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, email, password, **extra_fields)
    

class CustomUser(AbstractUser):
    # objects = CustomUserManager()
    pass
   
    


class Levels(models.Model):
    name=models.CharField(max_length=255)
    

    def __str__(self):
      return self.name
    

    
class Issues(models.Model):
    institution_name=models.CharField(max_length=100)
    email=models.EmailField()
    issue=models.CharField(max_length=200)
    level = models.ForeignKey(Levels, on_delete=models.SET_NULL, null=True, blank=True,default=8)
    status = models.IntegerField(choices=constants.COMPLAINT_STATUS_CHOICES,
                                 default=constants.COMPLAINT_STATUS_PENDING)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
     return self.institution_name
    
    def forward_to_next_level(self, next_level_number):
        try:
            next_level = Levels.objects.get(level_number=next_level_number)
            self.level = next_level
            self.save()
            return True
        except Levels.DoesNotExist:
            return False
    
    
    
    class Meta:
        ordering = ['-created_at']


class Solution(models.Model):
    issue = models.ForeignKey(Issues,  on_delete=models.CASCADE)
    answer=models.CharField(max_length=255)

    def __str__(self):
      return self.answer

class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    level = models.ForeignKey(Levels, on_delete=models.SET_NULL, null=True, blank=True)

    

    

