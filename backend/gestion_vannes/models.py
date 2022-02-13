
from pyexpat import model
from django.db import models

# Create your models here.
class Champ(models.Model):
    nomChamp=models.CharField(max_length=30 ,unique=True)
    address=models.CharField(max_length=50 ,unique=True)
    description=models.TextField(max_length=200 )
    cree_le=models.DateTimeField(auto_now_add=True)
    modifier_le=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomChamp

class Noeud(models.Model):
    nomNoeud=models.CharField(max_length=20)
    description=models.TextField(max_length=200 )
    valeur=models.FloatField()
    status=models.BooleanField(default=True)
    
    def __str__(self):
        return self.nomNoeud
class MicroControleur(models.Model):
    TYPES = [
        ('esp32', 'ESP32')
        
    ]
    nom=models.CharField(max_length=200)
    type = models.CharField(
        max_length=13,
        choices=TYPES,
        null=False, 
        blank=True,
        default="ESP32"
        )
