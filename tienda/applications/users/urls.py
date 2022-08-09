from unicodedata import name
from django import views
from django.urls import path
from .views import LoginUser, GoogleLoginView

app_name ='users_app'

urlpatterns = [
    path('login/', LoginUser.as_view(), name = 'login'),
    path('api/google-login/', GoogleLoginView.as_view(), name = 'users-google-login')
]