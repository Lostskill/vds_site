from django.contrib import admin
from django.urls import path
from .views import *
from main.views import *

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('category/<slug:cat_slug>/', RubList.as_view() ,name = 'rubrics'),
    path('card/<slug:card_slug>', ShowCard.as_view(), name = 'vcard')
]
