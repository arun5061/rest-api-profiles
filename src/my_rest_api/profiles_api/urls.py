from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
urlpatterns = [
    path('hello-view/', views.HelloApi.as_view(), name='test-api'),
    path('viewset/', include(router.urls))
]
