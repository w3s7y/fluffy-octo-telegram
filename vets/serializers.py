from rest_framework import serializers
from vets import models


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pet
        fields = '__all__'


class VetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vet
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Appointment
        fields = '__all__'
