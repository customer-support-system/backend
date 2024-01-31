from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,Permission,Group


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=30)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    

    def __str__(self):
        return self.username

    # Add the following lines to resolve the E304 error
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions',  # Change this to a unique name
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups',  # Change this to a unique name
    )

# Create your models here.
class Issues(models.Model):
    institution_name=models.CharField(max_length=100)
    email=models.EmailField()
    issue=models.CharField(max_length=200)

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

