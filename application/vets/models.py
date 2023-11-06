from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    SY = "Shropshire"
    CH = "Cheshire"
    GM = "Greater Manchester"
    ORG_AREA_CHOICES = [(SY, "Shropshire and North Wales"),
                        (CH, "Cheshire and Wirral"),
                        (GM, "Greater Manchester")]

    address_line_1 = models.CharField(max_length=200, blank=False, null=False)
    address_line_2 = models.CharField(max_length=200, blank=True)
    address_line_3 = models.CharField(max_length=200, blank=True)
    address_line_4 = models.CharField(max_length=200, blank=True)
    org_area = models.CharField(max_length=100, choices=ORG_AREA_CHOICES,
                                blank=False, null=False)
    post_code = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return f"{self.address_line_1} - {self.address_line_2} - " \
               f"{self.post_code} - {self.org_area}"


class Surgery(models.Model):
    name = models.CharField(max_length=200, blank=False,
                            null=False, unique=True)
    address = models.ForeignKey('Address', blank=False,
                                null=False, on_delete=models.RESTRICT)
    opening_time = models.TimeField(blank=False, null=False)
    closing_time = models.TimeField(blank=False, null=False)

    def __str__(self):
        return f"{self.name}"


class Human(User):
    middle_names = models.CharField(max_length=200, blank=True, null=True)
    home_address = models.ForeignKey('Address', blank=False,
                                     on_delete=models.RESTRICT, null=False)
    primary_contact_telephone = models.CharField(max_length=100,
                                                 blank=False, null=False)
    secondary_contact_telephone = models.CharField(max_length=100, blank=True)


class Vet(Human):
    salary = models.IntegerField(blank=False)
    notifications_enabled = models.BooleanField(default=True)
    base_surgery = models.ForeignKey('Surgery', on_delete=models.RESTRICT,
                                     null=False)

    def __str__(self):
        return f"{self.username} - {self.base_surgery.name}"


class Client(Human):
    registered_surgery = models.ForeignKey('Surgery', blank=False,
                                           on_delete=models.RESTRICT,
                                           null=False)

    def __str__(self):
        return f"{self.username} - {self.email} - {self.home_address.post_code}"


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
                               choices=SPECIES_CHOICES, null=False)
    dob = models.DateTimeField(blank=False, null=False)
    dod = models.DateTimeField(null=True, blank=True)
    chip_id = models.BigIntegerField(null=True)
    owner = models.ForeignKey('Client', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.name}"


class Appointment(models.Model):
    appointment_date_time = models.DateTimeField(blank=False, null=False)
    surgery = models.ForeignKey('Surgery', on_delete=models.CASCADE,
                                null=True)
    vet = models.ForeignKey('Vet', on_delete=models.CASCADE, null=False)
    client = models.ForeignKey('Client', on_delete=models.CASCADE,
                               null=False)
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE, null=False)
    details = models.TextField(default="Nature of Appointment: ")
    outcome = models.TextField(default="Outcomes / Future Treatments: ")

    def __str__(self):
        return f"{self.surgery} - {self.vet} - " \
               f"{self.pet} - {self.appointment_date_time.__str__()}"
