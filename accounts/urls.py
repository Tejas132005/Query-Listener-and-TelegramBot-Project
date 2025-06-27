from django.urls import path
from .views import RegisterAPI, LoginAPI, MainPage

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name="register"),
    path('login/', LoginAPI.as_view(), name='login'), 
]