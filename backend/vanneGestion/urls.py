
from django.urls import path

from backend.vanneGestion.views import CreateChamps



urlpatterns = [
    path('creerChamp',CreateChamps.asview()),
   
]