from django.shortcuts import render
from backend.vanneGestion.models import Champ, Vanne
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
    queryset=Vanne.objects.all()
    serializer_class=VanneSerializer