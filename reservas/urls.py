from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),

    # Rutas para los campistas
    path('campistas/', views.campista_list, name='campista_list'),
    path('campista/<int:id>/', views.campista_detail, name='campista_detail'),
    path('campista/nuevo/', views.campista_create, name='campista_create'),
    path('campista/<int:id>/editar/', views.campista_edit, name='campista_edit'),
    path('campista/<int:id>/eliminar/', views.campista_delete, name='campista_delete'),

    # Rutas para las reservas
    path('reservas/', views.reserva_list, name='reserva_list'),
    path('reserva/<int:id>/', views.reserva_detail, name='reserva_detail'),
    path('reserva/nueva/', views.reserva_create, name='reserva_create'),
    path('reserva/<int:id>/editar/', views.reserva_edit, name='reserva_edit'),
    path('reserva/<int:id>/eliminar/', views.reserva_delete, name='reserva_delete'),
]
