from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("akbar", views.akbar, name="akbar"),
    path("<str:name>", views.greet, name="greet")
]    
