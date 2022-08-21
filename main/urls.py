from django import views
from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('filter/', views.FilterCard.as_view() ,name = 'filter'),
    path('category/<slug:cat_slug>/', RubList.as_view() ,name = 'rubrics'),
    path('card/<slug:card_slug>', ShowCard.as_view(), name = 'vcard'),
    path('about/', About.as_view() , name = 'about'),
    path('login/', LoginUser.as_view() ,name = 'login'),
    path('register/', RegisterUser.as_view() ,name = 'register'),   
]
