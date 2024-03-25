"""
ticket number
feedback
time when it was created
report to admins about who forwarded the complaints and why??
"""
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from portal import constants


class Levels(models.Model):
    order = models.IntegerField(unique=True, null=True, blank=True)
    name=models.CharField(max_length=255)
    

    def __str__(self):
      return self.name
    
    class Meta:
        ordering = ['order']
    


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

      level = models.ForeignKey(Levels, on_delete=models.SET_NULL, null=True, blank=True)
   

class Issues(models.Model):
    institution_name=models.CharField(max_length=100)
    email=models.EmailField()
    issue=models.CharField(max_length=200)
    level = models.ForeignKey(Levels, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField(choices=constants.COMPLAINT_STATUS_CHOICES,
                                 default=constants.COMPLAINT_STATUS_PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
     return self.institution_name
    
    def save(self, **kwargs) -> None:
        if not self.level:
            first_level = Levels.objects.first()
            self.level = first_level
        return super().save(**kwargs)
    

    
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

    

    

