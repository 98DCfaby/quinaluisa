from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página de inicio
    path('inicio/', views.inicio, name='inicio'),
    path('campista/', views.nuevo_campista, name='nuevo_campista'),
    path('listadoCampista/', views.listar_campista, name='listar_campista'),
    path('guardarCampista/', views.guardar_campista, name='guardar_campista'),
]