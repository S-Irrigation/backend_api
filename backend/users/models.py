import email
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

#services=service.models.Service

class User(AbstractUser,models.Model):
    username=models.CharField(max_length=10 , unique=True)
    telephones = ArrayField(models.CharField(max_length=200), blank=True)
    USERNAME_FIELD = 'username'
    objects=UserManager()
    def __str__(self):
        return self.username