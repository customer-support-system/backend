from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,Permission,Group
from django.contrib.auth.hashers import make_password


class CustomUser(AbstractUser):
    
    pass

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        if password is not None:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)
    
class IssueQuerySet(models.QuerySet):
    def without_solutions(self):
        return self.annotate(solution_count=models.Count('solution')).filter(solution_count=0)
    
class Issues(models.Model):
    institution_name=models.CharField(max_length=100)
    email=models.EmailField()
    issue=models.CharField(max_length=200)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('answered', 'Answered'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
     return self.institution_name


class Levels(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
      return self.name


class Solution(models.Model):
    issue_id = models.ForeignKey(Issues, to_field='id', on_delete=models.CASCADE)
    answer=models.CharField(max_length=255)

    def __str__(self):
      return self.answer

class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    level = models.ForeignKey(Levels, on_delete=models.SET_NULL, null=True, blank=True)

