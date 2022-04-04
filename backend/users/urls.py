from knox import views as knox_views
from .views import AjoutNumero, DeleteNumber, DeleteUser,  LoginAPI, RegisterAPI, UpdateNumber, UpdateUser, UserAPI, ChangePasswordView, UserList
from django.urls import path

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('user/', UserAPI.as_view(), name='user'),
    path('deleteuser/<int:pk>', DeleteUser.as_view(({
        'delete':'delete',
    }))),
    path('deletelephone/<int:pk>', DeleteNumber.as_view(({
        'delete':'delete',
    }))),
     path('updateUser/<int:pk>', UpdateUser.as_view(({
        'put':'update',
    }))),
    path('updateTelephone/<int:pk>', UpdateNumber.as_view(({
        'put':'update',
    }))),
    
    path('listuser/' ,UserList.as_view()),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path("addnumber/", AjoutNumero.as_view({
        "post":"create"
    }))
    
    
]