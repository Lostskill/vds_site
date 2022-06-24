from django.contrib import admin
from django.urls import path
from .views import *
from main.views import *
urlpatterns = [
    path('', Main.as_view(), name='main'),
    #path('<slug>',name = 'rubrics')
]
