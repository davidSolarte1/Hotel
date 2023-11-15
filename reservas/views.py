from .models import Habitacion, Reserva, Cliente
from django.urls import reverse_lazy 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
#from django import forms

#Habitaciones

class HabitacionListView(ListView):
    model = Habitacion

class HabitacionDetailView(DetailView):
    model = Habitacion

class HabitacionCreate(CreateView):
    model = Habitacion
    fields = '__all__'

class HabitacionUpdate(UpdateView):
    model = Habitacion
    fields = '__all__' 

class HabitacionDelete(DeleteView):
    model = Habitacion
    success_url = reverse_lazy('habitacion-list')
#Reservas

class ReservaListView(ListView):
    model = Reserva

class ReservaDetailView(DetailView):
    model = Reserva

class ReservaCreate(CreateView):
    model = Reserva
    fields = '__all__'

class ReservaUpdate(UpdateView):
    model = Reserva
    fields = '__all__' 

class ReservaDelete(DeleteView):
    model = Reserva
    success_url = reverse_lazy('reserva-list')
#Clientes

class ClienteListView(ListView):
    model = Cliente

class ClienteDetailView(DetailView):
    model = Cliente

class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = '__all__' 

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente-list')