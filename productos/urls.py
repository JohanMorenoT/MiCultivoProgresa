from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio , name="inicio.html")
]