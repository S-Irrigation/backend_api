from django.shortcuts import render
from rest_framework import generics, serializers ,viewsets,permissions
from rest_framework.response import Response

from Smart_irriagation.backend.gestion_vannes.models import Champ ,Vanne, Capteur
from Smart_irriagation.backend.gestion_vannes.serializers import CapteurSerializer, ChampsSerializer, VanneSerializer
# Create your views here.
class CreateChamps(generics.CreateAPIView):
    querySet=Champ.objects.all()
    serializer_class=ChampsSerializer

class RUDChamp(generics.RetrieveUpdateAPIView):
    querySet=Champ.objects.all()
    serializer_class=ChampsSerializer

class ListChamp(viewsets.ViewSet):
    def get(self,request):
        querySet=Champ.objects.all()
        serializer=ChampsSerializer(querySet,many=True)
        return Response(serializer.data)
class CreateVanne(generics.CreateAPIView):
    queryset=Vanne.objects.all()
    serializer_class=VanneSerializer

class RUDVanne(generics.RetrieveUpdateAPIView):
    querySet=Vanne.objects.all()
    serializer_class=VanneSerializer

class ListVanne(viewsets.ViewSet):
    def get(self, request):
        querySet=Vanne.objects.all()
        serializer=VanneSerializer(querySet,many=True)
        return Response(serializer.data)
class CreateCapteur(generics.CreateAPIView):
    querySet=Capteur.objects.all()
    serializer_class=CapteurSerializer
class RUDCapteur(generics.RetrieveUpdateAPIView):
    querySet=Capteur.objects.all()
    serializer_class=CapteurSerializer
