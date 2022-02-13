from pyexpat import model
from attr import fields
from rest_framework import serializers

from gestionVannes.models import Capteur, Champ, MicroControleur, Noeud, Vanne

class ChampsSerializer(serializers.ModelSerializer):
   class Meta:
       model=Champ
       fields=('nomChamp','address','proprietaire','description','creer_le' ,'modifier_le')
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
class Microcontroleur(serializers.ModelSerializer):
    class Meta:
        model=MicroControleur
        fields=('nomMicrocontroleur','type')