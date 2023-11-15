"""
URL configuration for hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reservas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('habitacion/', views.HabitacionListView.as_view(), name='habitacion-list'),
    path('habitacion/add/', views.HabitacionCreate.as_view() , name='habitacion-create'),
    path('habitacion/<int:pk>/detail/', views.HabitacionDetailView.as_view(), name='habitacion-detail'),
    path('habitacion/<int:pk>/update/',views.HabitacionUpdate.as_view(),name='habitacion-update'),
    path('habitacion/<int:pk>/delete/', views.HabitacionDelete.as_view(), name='habitacion-delete'),

    path('habitacion/reservar/', views.ReservaCreate.as_view() , name='reserva-create'),
    path('reserva/', views.ReservaListView.as_view() , name='reserva-list'),
    path('reserva/<int:pk>/detail/', views.ReservaDetailView.as_view() , name='reserva-detail'),
    path('reserva/<int:pk>/update/', views.ReservaUpdate.as_view() , name='reserva-update'),
    path('reserva/<int:pk>/delete/', views.ReservaDelete.as_view(), name='reserva-delete'),

    path('cliente/', views.ClienteListView.as_view(), name='cliente-list'),
    path('cliente/add/', views.ClienteCreate.as_view() , name='cliente-create'),
    path('cliente/<int:pk>/detail/', views.ClienteDetailView.as_view(), name='cliente-detail'),
    path('cliente/<int:pk>/update/',views.ClienteUpdate.as_view(),name='cliente-update'), 
    path('cliente/<int:pk>/delete/', views.ClienteDelete.as_view(), name='cliente-delete'),

    #path('habitacion/<int:habitacion_id>/reservar/', reservar_habitacion, name='reservar_habitacion'),
]
