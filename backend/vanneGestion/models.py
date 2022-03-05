from django.db import models

# Create your models here.
class Champ(models.Model):
    nomChamp=models.CharField(max_length=30 ,unique=True)
    proprietaire=models.ForeignKey('users.User',on_delete=models.CASCADE)
    address=models.CharField(max_length=50 ,unique=True)
    description=models.TextField(max_length=200 )
    creer_le=models.DateTimeField(auto_now_add=True)
    modifier_le=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomChamp

class Noeud(models.Model):
    champ=models.ForeignKey(Champ ,on_delete=models.CASCADE ,default=0)
    nomNoeud=models.CharField(max_length=20)
    description=models.TextField(max_length=200 )
    class Meta:
        abstract = True
class Vanne(Noeud):
    status=models.BooleanField(default=False)
    debut=models.DateTimeField()
    fin=models.DateTimeField()
    
    def __str__(self) :
        return super().nomNoeud
class Capteur(Noeud):
    valeur=models.FloatField()
    
    def __str__(self):
        return super().nomNoeud
class MicroControleur(models.Model):
    TYPES = [
        ('esp32', 'ESP32')
        
    ]
    nomMicrocontroleur=models.CharField(max_length=200)
    type = models.CharField(
        max_length=13,
        choices=TYPES,
        null=False, 
        blank=True,
        default="ESP32"
        )
