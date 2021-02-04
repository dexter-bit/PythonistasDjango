from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/',  views.agregar,  name="agregar"),
    path('ordenar/',  views.ordenar,  name="ordenar")
]