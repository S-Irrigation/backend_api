from django.shortcuts import render
from vanneGestion.models import Champ, Vannes
from vanneGestion.serializers import ChampsSerializer, VanneSerializer
from rest_framework import generics, serializers ,viewsets,permissions
from rest_framework.response import Response

# Create your views here.
class CreateChamps(generics.CreateAPIView):
    queryset=Champ.objects.all()
    serializer_class=ChampsSerializer

class RUDChamps(generics.RetrieveUpdateDestroyAPIView):
    queryset=Champ.objects.all()
    serializer_class=ChampsSerializer
class ListChamps(viewsets.ViewSet):
    def get(self ,request):
        queryset=Champ.objects.all()
        serializer=ChampsSerializer(queryset,many=True)
        return Response(serializer.data)
class CreateVanne(generics.CreateAPIView):
    queryset=Vannes.objects.all()
    serializer_class=VanneSerializer
class RUDVanne(generics.RetrieveUpdateDestroyAPIView):
    queryset=Vannes.objects.all()
    serializer_class=VanneSerializer

class ListVanne(viewsets.ViewSet):
    def get(self ,request):
        queryset=Vannes.objects.all()
        serializer=VanneSerializer(queryset,many=True)
        return Response(serializer.data)
class ActivateVanne(viewsets.ViewSet):
    def get (self , request):
        queryset=Vannes.objects.filter(status=True)
        serializer=VanneSerializer(queryset , many=True)
        return Response(serializer.data)
class Unactivatevanne(viewsets.ViewSet):
    def get(self , request):
        queryset=Vannes.objects.filter(status=False)
        serializer=VanneSerializer(queryset,many=True)
        return Response(serializer.data)