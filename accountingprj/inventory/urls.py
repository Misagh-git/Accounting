from django.urls import path
from .views import display



urlpatterns = [
    path('', display),
]