from this import d
from django.contrib.auth import login
from django.db.models import query
from rest_framework import serializers, views, viewsets
from .models import Telephone, User
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import TelephoneSerializer, UserSerializer, RegisterSerializer, ChangePasswordSerializer
from django.views.decorators.debug import sensitive_post_parameters

from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.decorators import api_view
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    

class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()

class AjoutNumero(viewsets.ViewSet):
    def create(self, request):
        serializer = TelephoneSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class DeleteNumber(viewsets.ViewSet):
    def delete(self ,request ,pk=None):
        querySet=Telephone.objects.get(id=pk)
        querySet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
class UpdateUser(viewsets.ViewSet):
    def update(self ,request ,pk=None):
        query=User.objects.get(id=pk)
        serializers=UserSerializer(query, partial=True)
        return Response(serializers.data)
 
class UpdateNumber(viewsets.ViewSet):
    def update(self ,request ,pk=None):
        query=Telephone.objects.get(id=pk)
        serializers=UserSerializer(query, partial=True)
        return Response(serializers.data)
 
class DeleteUser(viewsets.ViewSet):
    def delete(self , request ,pk=None):
        querySet=User.objects.get(id=pk)
        querySet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
        
         
from rest_framework import generics, permissions

# Change Password
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer, RegisterSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated   

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

