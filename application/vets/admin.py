from django.contrib import admin
from vets.models import Address, Pet, Appointment, Surgery, Client, Vet

# Registering our models with the django
# admin site so we can view/edit the data/users there.
admin.site.register([Address, Pet, Appointment, Surgery, Client, Vet])
