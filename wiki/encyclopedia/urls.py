from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entries/<str:title>", views.entries, name="entries"),
    path("search", views.search, name="search"),
]
