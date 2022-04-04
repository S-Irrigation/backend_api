from dataclasses import fields
from rest_framework import generics, permissions
from rest_framework import serializers
from .models import Telephone, User

from django.contrib.auth import get_user_model
User = get_user_model()

#Telephone Serializer
class TelephoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Telephone
        fields=("numero")

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email' ,'last_name' , 'first_name' )

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password' , 'last_name' , 'first_name',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(self.validated_data ['username'],  
        self.validated_data['email'], self.validated_data['password']  , last_name=validated_data['last_name'], first_name=validated_data['first_name'] )

        return user

# Change Password
from rest_framework import serializers
from django.contrib.auth.models import User

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
