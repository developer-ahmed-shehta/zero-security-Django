from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.search_form, name='search_form'),
    path('get_user/', views.get_user, name='get_user'),
]
