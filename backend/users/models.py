import email
from django.db import models
#from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.

class User(AbstractUser,models.Model):
    username=models.CharField(max_length=10 , unique=True)
    telephones=models.ManyToManyField("Telephone",blank=True)
    USERNAME_FIELD = 'username'
    objects=UserManager()
    def __str__(self):
        return self.username
class Telephone(models.Model):
    numero=models.IntegerField(unique=True)
    def __str__(self):
        return str(self.numero)