from rest_framework import serializers
from .models import Cliente,Habitacion,Reserva


class HabitacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Habitacion
        fields = ('__all__')

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('__all__')

class ReservaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reserva
        fields = ('__all__')