from django.urls import path, include
from . import views

urlpatterns = [
    path('hello-view/', views.HelloApi.as_view(), name='test-api'),
]
