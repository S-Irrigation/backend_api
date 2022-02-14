
from django.urls import path

from vanneGestion.views import CreateChamps, ListChamps, RUDChamps



urlpatterns = [
    path('creerChamp',CreateChamps.as_view()),
    path('champ/<int:pk>' ,RUDChamps.as_view()),
    path('listChamp/' ,ListChamps.as_view({
        'get':'get'
    }))
   
]