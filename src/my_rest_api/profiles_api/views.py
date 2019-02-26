from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApi(APIView):

    def get(self, requests, format=None):

        an_apiview = [
            'Uses HTTP methods as functions(get, put, post, patch, delete)',
            'It is similar to Traditional Django View',
            'Is mapped manually to URLs'
        ]

        return Response({'an_api': an_apiview, 'msg':'Hello'})