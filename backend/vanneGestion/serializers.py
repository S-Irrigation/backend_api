from pyexpat import model
from attr import fields

from rest_framework import serializers

from vanneGestion.models import Capteur, Champ, MicroControleur, Noeud, Vannes

class ChampsSerializer(serializers.ModelSerializer):
   class Meta:
       model=Champ
       fields=('id' ,'nomChamp','address','proprietaire','description','creer_le' ,'modifier_le')
class NoeudSerializer(serializers.ModelSerializer):
    class Meta:
        model=Noeud
        fields=('nomNoeud')
class VanneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vannes
        fields=('id','status' ,'nomNoeud', 'champ' , 'start' ,'end')

class CapteurSerializer(serializers.ModelSerializer):
    class Meta:
        model=Capteur
        fields=('valeur','Nomnoeud','champ')
class Microcontroleur(serializers.ModelSerializer):
    class Meta:
        model=MicroControleur
        fields=('nomMicrocontroleur','type')