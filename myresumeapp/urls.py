from django.contrib import admin
from django.urls import path
from .views import hellostudent

urlpatterns = [
    path('mainpage/', hellostudent),
]
