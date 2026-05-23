from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),          # rota principal → home.html
    path('inicio/', views.inicio, name='inicio'),  # rota inicio → inicio.html
]
