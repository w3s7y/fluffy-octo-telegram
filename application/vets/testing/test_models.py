from django.test import TestCase
from vets.models import Surgery
from vets.models import Pet
from vets.models import Vet
from vets.models import Appointment
from vets.models import Client


class TestModels(TestCase):
    def setUp(self):
        self.s1 = Surgery.objects.create(name="Oak",
                                         opening_time="09:00:00", closing_time="17:30:00")
        self.s2 = Surgery.objects.create(name="Banana",
                                         opening_time="08:00:00", closing_time="17:30:00")

        self.v1 = Vet.objects.create(primary_contact_telephone="0792342331222",
                                     salary="54000", base_surgery=Surgery.objects.get(name="Oak"),
                                     username="vet1")
        self.v2 = Vet.objects.create(primary_contact_telephone="0792342331333",
                                     salary="54000", base_surgery=Surgery.objects.get(name="Banana"),
                                     username="vet2")
        self.c1 = Client.objects.create(username="client1")
        self.c2 = Client.objects.create(username="client2")
        self.c3 = Client.objects.create(username="client3")

        self.p1 = Pet.objects.create(dob="2023-03-01 12:00:00Z", name="Jimmy", )

    def test_db_basic_surgery(self):
        oak = Surgery.objects.get(name="Oak")
        ban = Surgery.objects.get(name="Banana")
        self.assertFalse(oak == ban)


