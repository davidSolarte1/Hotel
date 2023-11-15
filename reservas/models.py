from django.db import models
from django.urls import reverse
# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('cliente-list')

class Habitacion(models.Model):
    numero = models.CharField(max_length=3)
    tipo = models.CharField(max_length=100,  blank=True)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.numero
        
    def get_absolute_url(self):
        return reverse('habitacion-list')

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()

    # def __str__(self):
    #     return self.cliente
    def get_absolute_url(self):
        return reverse('reserva-list')