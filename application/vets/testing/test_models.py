from unittest import TestCase
from vets.models import *


class TestAddress(TestCase):
    def test_address_data_loaded_from_runner(self):
        self.assertTrue(Address.objects.all())

    def test_good_count_of_addresses(self):
        self.assertEqual(len(Address.objects.all()), 11)

    def test_create_duplicate_address_fails(self):
        """
        Probably not working the way I expect.  Suspect we can only have row level validation at this (model) level
        and multi-row validation (checking the entire address is unique).
        Returns:

        """
        addr = {
            "address_line_1": "1 Darwin Way",
            "address_line_2": "Shrewsbury Business Park",
            "address_line_3": "Shrewsbury",
            "address_line_4": "",
            "post_code": "SY3 2WK",
            "org_area": Address.SY
        }
        qset = Address.objects.filter(**addr)
        qset[0].id = None
        qset[0].save()

        self.assertNotEqual(len(Address.objects.all()), 12)


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
