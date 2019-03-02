from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login',views.LoginViewSet, base_name='login')
router.register('status', views.StatusViewSet, base_name='status')

urlpatterns = [
    path('hello-view/', views.HelloApi.as_view(), name='test-api'),
    path('viewset/', include(router.urls))
]
