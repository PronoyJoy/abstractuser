from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from .manager import UserManager
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'

    object = UserManager()

    REQUIRED_FIELDS = ['password']
