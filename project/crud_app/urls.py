from django.urls import path
from .models import User
from .views import UserAPI, UserDetailsAPI

urlpatterns = [
    path('user/', UserAPI.as_view()),
    path('user/<int:pk>/', UserDetailsAPI.as_view())
]