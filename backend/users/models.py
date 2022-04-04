import email
from django.db import models
#from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.
class Telephone(models.Model):
    numero=models.IntegerField(max_length=8 ,unique=True)
    def __str__(self):
        return self.numero
class User(AbstractUser,models.Model):
    username=models.CharField(max_length=10 , unique=True)
    USERNAME_FIELD = 'username'
    telephones=models.ManyToManyField(Telephone ,null=True)
    objects=UserManager()
    def __str__(self):
        return self.username
