from unittest import TestCase
from vets.models import *


class TestAddress(TestCase):
    def test_address_data_loaded_from_runner(self):
        self.assertTrue(Address.objects.all())

    def test_good_count_of_addresses(self):
        self.assertEqual(len(Address.objects.all()), 11)

    def test_equality_function(self):
        """
        Probably not working the way I expect.  Suspect we can only have row level validation at this (model) level
        and multi-row validation (checking the entire address is unique).
        Returns:

        """
        duplicate_addr = {
            "address_line_1": "1 Darwin Way",
            "address_line_2": "Shrewsbury Business Park",
            "address_line_3": "Shrewsbury",
            "address_line_4": "",
            "post_code": "SY3 2WK",
            "org_area": Address.SY
        }
        result = Address.objects.filter(**duplicate_addr)[0]
        local_address = Address(**duplicate_addr)
        # local_address.save()
        new_set = Address.objects.all()
        print(new_set, local_address.id)
        self.assertEqual(result, local_address)


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
