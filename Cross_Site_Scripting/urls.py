# Cross_Site_Scripting/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("stored/", views.stored_xss, name="stored_xss"),
    path("reflected/", views.reflected_xss, name="reflected_xss"),
    path("xss_demo_action/", views.xss_demo_action, name="xss_demo_action"),
    
]
