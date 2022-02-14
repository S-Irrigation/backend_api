
from django.urls import path

from vanneGestion.views import CreateChamps, ListChamps, RUDChamps



urlpatterns = [
    path('creerChamp',CreateChamps.asview()),
    path('champ/<int:pk>' ,RUDChamps.asview()),
    path('listChamp/' ,ListChamps.asview({
        'get':'get'
    }))
   
]