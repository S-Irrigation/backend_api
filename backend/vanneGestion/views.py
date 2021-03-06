from functools import partial
from logging import raiseExceptions
from django.shortcuts import render
from vanneGestion.models import Champ, Vannes
from vanneGestion.serializers import ChampsSerializer, VanneSerializer
from rest_framework import generics, serializers ,viewsets,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime 
from datetime import datetime
from dateutil import tz

from datetime import timedelta
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

@api_view(["POST"])
def  activationManuel(request ,id):
    vanne=Vannes.objects.get(id=id)
    #vanne.start=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    vanne.start = datetime.today().astimezone(tz=tz.gettz('Europe/Paris')).strftime("%Y-%m-%dT%H:%M:%S")
    vanne.end=datetime(2080, 4, 2, 21, 8, 8).strftime("%Y-%m-%dT%H:%M:%S")
    vanne.save()
    serializers=VanneSerializer(vanne, partial=True)
    return Response(serializers.data)




@api_view(["POST"])
def  activationAutomatique(request ,id, date, duration):
    vanne=Vannes.objects.get(id=id)   
    date_time_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
    vanne.start = date_time_obj
    data = duration.split(":")
    vanne.end = date_time_obj + timedelta(hours=int(data[0]), minutes=int(data[1]))
    vanne.save()
    serializers=VanneSerializer(vanne, partial=True)
    return  Response(serializers.data)





@api_view(["POST"])
def desactivation(request , id):
    vanne=Vannes.objects.get(id=id)
    vanne.end=datetime.today().astimezone(tz=tz.gettz('Europe/Paris')).strftime("%Y-%m-%dT%H:%M:%S")
    vanne.start=vanne.end
    vanne.save()
    serializers=VanneSerializer(vanne, partial=True)
    return Response(serializers.data)


@api_view(["GET"])
def getidChamp(request ,nomChamp):
    champ=Champ.objects.get(nomChamp=nomChamp)
    return Response({
        "id":champ.id
    })
        
