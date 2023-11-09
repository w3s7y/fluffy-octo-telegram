from rest_framework import serializers
import vets


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = vets.models.Client
        fields = '__all__'


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = vets.models.Pet
        fields = '__all__'


class VetSerializer(serializers.ModelSerializer):
    class Meta:
        model = vets.models.Vet
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = vets.models.Appointment
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = vets.models.Address
        fields = '__all__'


class SurgerySerializer(serializers.ModelSerializer):
    class Meta:
        model = vets.models.Surgery
        fields = '__all__'
