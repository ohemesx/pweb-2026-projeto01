from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("inicio/", views.inicio, name="inicio"),
    path("elenco/", views.elenco, name="elenco"),
    path("sobre/", views.sobre, name="sobre"),
]
