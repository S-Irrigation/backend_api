from django import urls


from django.urls import path

from Smart_irriagation.backend.gestion_vannes.views import CreateChamps, ListChamp, ListVanne, RUDChamp, RUDVanne

urlpatterns = [
    path('champ',CreateChamps.as_view()),
    path('champ/<int:pk>' , RUDChamp.as_view()),
    path('listChamps/' ,ListChamp.as_view(
      {'get':'get'}  
    )), 
    path('vanne',CreateChamps.as_view()),
    path('vanne/<int:pk>' , RUDVanne.as_view()),
    path('listVanne/' ,ListVanne.as_view({
        'get':'get'
    })),
    
]