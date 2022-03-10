import email
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.
class User(AbstractUser,models.Model):
    username=models.CharField(max_length=10 , unique=True)
    telephones = ArrayField(models.CharField(max_length=5),default=list)
    USERNAME_FIELD = 'username'
    objects=UserManager()
    def __str__(self):
        return self.username