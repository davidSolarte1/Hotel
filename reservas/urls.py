from django.urls import path, include
from rest_framework import routers
from reservas import views

router = routers.DefaultRouter()
router.register(r'habitacion_rest', views.HabitacionViewSet)
router.register(r'cliente_rest', views.ClienteViewSet)
router.register(r'reserva_rest', views.ReservaViewSet)

urlpatterns=[
    

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
    
    path('api/', include(router.urls)),
    

]