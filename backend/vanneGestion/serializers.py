from pyexpat import model
from attr import fields
from rest_framework import serializers

from vanneGestion.models import Capteur, Champ, MicroControleur, Noeud, Vanne

class ChampsSerializer(serializers.ModelSerializer):
   class Meta:
       model=Champ
       fields=('id' ,'nomChamp','address','proprietaire','description','creer_le' ,'modifier_le')
class NoeudSerializer(serializers.ModelSerializer):
    class Meta:
        model=Noeud
        fields=('nomNoeud', 'description')
class VanneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vanne
        fields=('id','status' ,'nomNoeud' , 'champ' , 'debut' ,'fin')

class CapteurSerializer(serializers.ModelSerializer):
    class Meta:
        model=Capteur
        fields=('valeur','Nomnoeud','champ')
class Microcontroleur(serializers.ModelSerializer):
    class Meta:
        model=MicroControleur
        fields=('nomMicrocontroleur','type')