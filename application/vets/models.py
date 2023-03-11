from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    SY = "Shropshire"
    CH = "Cheshire"
    ORG_AREA_CHOICES = [(SY, "Shropshire and North Wales"),
                        (CH, "Cheshire and Wirral")]

    address_line_1 = models.CharField(max_length=200, blank=False)
    address_line_2 = models.CharField(max_length=200, blank=True)
    address_line_3 = models.CharField(max_length=200, blank=True)
    address_line_4 = models.CharField(max_length=200, blank=True)
    org_area = models.CharField(max_length=100, choices=ORG_AREA_CHOICES,
                                blank=False)
    post_code = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return f"{self.address_line_1} - {self.address_line_2} - " \
               f"{self.post_code}"


class Surgery(Address):
    name = models.CharField(max_length=200, blank=False, null=True)
    opening_time = models.TimeField(blank=False)
    closing_time = models.TimeField(blank=False)

    def __str__(self):
        return f"{self.name}"


class Human(User):
    middle_names = models.CharField(max_length=200, default="")
    home_address = models.ForeignKey('Address', blank=False,
                                     on_delete=models.RESTRICT, null=True)
    primary_contact_telephone = models.CharField(max_length=100, blank=False)
    secondary_contact_telephone = models.CharField(max_length=100, blank=True)


class Client(Human):
    def __str__(self):
        return f"{self.first_name} {self.middle_names} " \
               f"{self.last_name} - {self.home_address.post_code}"


class Pet(models.Model):
    DOG = "Canine"
    CAT = "Feline"
    HORSE = "Equidae"
    SPECIES_CHOICES = [
        (DOG, "Canine"),
        (CAT, "Feline"),
        (HORSE, "Equidae")
    ]

    name = models.CharField(max_length=100, blank=False)
    species = models.CharField(max_length=200, blank=False,
                               choices=SPECIES_CHOICES, null=True)
    dob = models.DateTimeField()
    dod = models.DateTimeField(null=True)
    chip_id = models.BigIntegerField(null=True)
    owner = models.ForeignKey('Client', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name}"


class Vet(Human):
    salary = models.IntegerField(blank=False)
    notifications_enabled = models.BooleanField(default=True)
    base_surgery = models.ForeignKey('Surgery', on_delete=models.RESTRICT,
                                     null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Appointment(models.Model):
    appointment_date_time = models.DateTimeField(blank=False)
    surgery = models.ForeignKey('Surgery', on_delete=models.RESTRICT,
                                null=True)
    vet = models.ForeignKey('Vet', on_delete=models.RESTRICT, null=True)
    client = models.ForeignKey('Client', on_delete=models.RESTRICT,
                               null=True)
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE, null=True)
    details = models.TextField(default="")

    def __str__(self):
        return f"{self.surgery} - {self.vet} - " \
               f"{self.pet} - {self.appointment_date_time.__str__()}"
