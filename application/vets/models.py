from django.db import models


class Human(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    address = models.TextField()
    primary_contact = models.IntegerField()
    secondary_contact = models.IntegerField()
    date_joined = models.DateTimeField(auto_now_add=True)


class Client(Human):
    pass


class Vet(Human):
    salary = models.IntegerField(blank=False)


class Pet(models.Model):
    name = models.CharField(max_length=100, blank=False)
    dob = models.DateTimeField()


class Appointment(models.Model):
    appointment_date_time = models.DateTimeField(blank=False)
    client = Client()
    vet = Vet()
    surgery = models.CharField(max_length=100)
