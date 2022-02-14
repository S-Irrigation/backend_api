"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.schemas import get_schema_view # new
from rest_framework import permissions # new
from drf_yasg.views import get_schema_view # new
from drf_yasg import openapi # new

schema_view = get_schema_view( # new
openapi.Info(
title="We Report It ",
default_version="v1",
description="""Gestion d' un systeme d' irrigation Projet Annuel Cette documentatio,n decrit les API utiliser Pour cela  """,
terms_of_service="http://sciences-techniques.univ-rouen.fr/master-informatique-genie-de-l-informatique-logicielle-543237.kjsp?RH=1378324428882",
contact=openapi.Contact(email="luc-perin.panta-pameni@univ-rouen.fr"),
license=openapi.License(name="Université de Rouen"),
),
public=True,
permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestVannes/' , include('vanneGestion.urls')),
    path('users/', include('users.urls')),
    path('swagger/', schema_view.with_ui( # new
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui( # new
'redoc', cache_timeout=0), name='schema-redoc'),
]
