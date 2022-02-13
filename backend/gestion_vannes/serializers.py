from pyexpat import model
from attr import fields
from rest_framework import serializers

from Smart_irriagation.backend.gestion_vannes.models import Capteur, Champ, MicroControleur, Noeud, Vanne

class ChampsSerializer(serializers.ModelSerializer):
   class Meta:
       model=Champ
       fields=('nomChamp','adress','proprietaire','description','creer_le' ,'modifier_le')
class NoeudSerializer(serializers.ModelSerializer):
    class Meta:
        model=Noeud
        fields=('nomNoeud', 'description')
class VanneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vanne
        fields=('status' ,'nomNoeud')

class CapteurSerializer(serializers.ModelSerializer):
    class Meta:
        model=Capteur
        fields=('valeur','Nomnoeud')
class Microcontromeur(serializers):
    class Meta:
        model=MicroControleur
        fields=('nomMicrocontroleur','type')