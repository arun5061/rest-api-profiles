from django.shortcuts import render
from . import serializers
from . import models
from . import permissions

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class HelloApi(APIView):

    serializer_class = serializers.HelloSerializer
    def get(self, requests, format=None):
        an_apiview = [
            'Uses HTTP methods as functions(get, put, post, patch, delete)',
            'It is similar to Traditional Django View',
            'Is mapped manually to URLs'
        ]
        return Response({'an_api': an_apiview, 'msg':'Hello', 'method':'get'})

    def post(self, requests):
        print('ser_data:', requests.data)
        ser_data = serializers.HelloSerializer(data=requests.data)
        if ser_data.is_valid():
            name = ser_data.data.get('name')
            message = 'Hello {} welcome to first Serializer tuto'.format(name)
            return Response({'message': message})
        else:
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, requests):

        return Response({'method1':'put'})
    def patch(self, requests):

        return Response({'method2':'patch'})

    def delete(self, requests):

        return Response({'method3':'delete'})

class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer
    """View set for CURD"""
    def list(self, requests):
        a_viewset=[
            "User actions (list, create, retrieve, update, partial_update )",
            "Automatically maps to URLs using Routers",
            "Provides more functionalies than APIViews",
        ]
        return Response({'msg':'Hey Arun, Ur first viewset', 'a_viewset': a_viewset})

    def create(self, requests):
        view_data = serializers.HelolSerializer(data=requests.data)
        if view_data.is_valid():
            mail = view_data.data.get('mail')
            msg = 'Hey my {} id'.format(mail)
            return Response({'mail_id':mail, 'msg':msg})
        else:
            return Response(view_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, requests, pk=None):

        return Response({'method1':'Get'})
    def update(self, requests, pk=None):

        return Response({'method2':'update'})

    def partial_update(self, requests, pk=None):

        return Response({'method2':'PATCH'})

    def destroy(self, requests, pk=None):

        return Response({'method3':'delete'})

class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().post(request)

class StatusViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.OwnStatusUpdate, IsAuthenticated)
    serializer_class = serializers.StatusSerializer
    queryset = models.ProfileStatus.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('status_tag', 'status_text',)

    def perform_create(self, serializer):
        serializer.save(user_profile = self.request.user)
        user_profile = self.request.user
        print('user_profile:', user_profile)


