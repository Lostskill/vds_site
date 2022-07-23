from django import views
from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('category/<slug:cat_slug>/', RubList.as_view() ,name = 'rubrics'),
    path('card/<slug:card_slug>', ShowCard.as_view(), name = 'vcard'),
    path('about/', views.about , name = 'about'),
    path('login/', LoginUser.as_view() ,name = 'login'),
    path('register/', RegisterUser.as_view() ,name = 'register'),
]
