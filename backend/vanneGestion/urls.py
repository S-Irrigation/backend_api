
from django.urls import path
 
from vanneGestion.views import CreateVanne, ListVanne, RUDVanne ,ActivateVanne, Unactivatevanne, activationManuel, getidChamp

from vanneGestion.views import CreateChamps, ListChamps, RUDChamps



urlpatterns = [
    path('creerChamp',CreateChamps.as_view()),
    path('champ/<int:pk>' ,RUDChamps.as_view()),
    path('listChamp/' ,ListChamps.as_view({
        'get':'get'
    })),
    #### Gestion des vannes 
    path('creerVanne' ,CreateVanne.as_view()),
    path('vanne/<int:pk>',RUDVanne.as_view()),
    path('listVanne/' ,ListVanne.as_view({
        'get':'get'
    })),
    path('activeVannne/',ActivateVanne.as_view({
        'get':'get'
    })),
    path('unactiveVanne/',Unactivatevanne.as_view({
        'get':'get'
    })),
    path('getIdChampByName/<str:nomChamp>' ,getidChamp),
    path('activationmanuelle/<in:id>' ,activationManuel)
   
]