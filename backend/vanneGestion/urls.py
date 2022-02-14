
from django.urls import path

from backend.vanneGestion.views import CreateChamps, ListChamps, RUDChamps



urlpatterns = [
    path('creerChamp',CreateChamps.asview()),
    path('champ/<int:pk>' ,RUDChamps.asview()),
    path('listChamp/' ,ListChamps.asview({
        'get':'get'
    }))
   
]