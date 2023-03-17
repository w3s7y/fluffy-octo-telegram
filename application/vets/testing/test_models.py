from django.test import TestCase
from vets.models import Surgery
from vets.models import Pet
from vets.models import Vet
from vets.models import Appointment
from vets.models import Client
from vets.models import Address


class TestAddress(TestCase):
    def test_address_data_loaded_from_runner(self):
        self.assertTrue(Address.objects.filter())

    def test_good_count_of_addresses(self):
        self.assertEqual(len(Address.objects.filter()), 11)


class TestSurgery(TestCase):
    def test_surgery_data_loaded_from_runner(self):
        self.assertTrue(Surgery.objects.filter())


class TestClient(TestCase):
    def test_client_data_loaded_from_runner(self):
        self.assertTrue(Client.objects.filter())


class TestPet(TestCase):
    def test_pet_data_loaded_from_runner(self):
        self.assertTrue(Pet.objects.filter())


class TestVet(TestCase):
    def test_vet_data_loaded_from_runner(self):
        self.assertTrue(Vet.objects.filter())


class TestAppointment(TestCase):
    def test_appointment_data_loaded_from_runner(self):
        self.assertTrue(Appointment.objects.filter())
