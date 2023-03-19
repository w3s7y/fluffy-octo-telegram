from django.test.runner import DiscoverRunner
from vets.models import *
import vets.testing.test_data as td
from django.contrib.auth.models import Group


class VetsTestRunner(DiscoverRunner):
    """
    Custom test runner for the Vets application.
    """
    def setup_databases(self, **kwargs):
        """
        Create an admin user and inject some test data to
        the DB before TestCases fire up.
        :param kwargs:
        :return:
        """
        super_init = super(VetsTestRunner, self).setup_databases(**kwargs)

        for group in td.VetsTestData.AUTH_GROUPS:
            Group.objects.create(name=group)

        for surgery in td.VetsTestData.SURGERIES:
            surg_to_make = {
                "name": surgery.pop("surgery_name"),
                "opening_time": surgery.pop("opening_time"),
                "closing_time": surgery.pop("closing_time")
            }
            address = Address.objects.create(**surgery)
            Surgery.objects.create(**surg_to_make, address=address)

        for client in td.VetsTestData.CLIENTS:
            usern = client.pop("client_username")
            surgery = client.pop("registered_surgery")
            address = Address.objects.create(**client)
            Client.objects.create_user(
                username=usern,
                email=f"{usern}@vets.internal",
                home_address=address,
                registered_surgery=Surgery.objects.get(name=surgery)
            )

        for vet in td.VetsTestData.VETS:
            vet_username = vet.pop("vet_username")
            base = vet.pop("base_surgery")
            salary = vet.pop("salary")
            address = Address.objects.create(**vet)
            Vet.objects.create_user(
                username=vet_username,
                email=f"{vet_username}@vets.internal",
                base_surgery=Surgery.objects.get(name=base),
                home_address=address,
                salary=salary
            )

        for pet in td.VetsTestData.PETS:
            owner = Client.objects.get(username=pet.pop("owner"))
            Pet.objects.create(**pet, owner=owner)

        for appt in td.VetsTestData.APPOINTMENTS:
            vet = Vet.objects.get(username=appt.pop("vet"))
            cli = Client.objects.get(username=appt.pop("client"))
            pet = Pet.objects.get(name="Barbara", owner=cli)
            Appointment.objects.create(
                appointment_date_time=appt.pop("appointment_date_time"),
                vet=vet, pet=pet, client=cli, details=appt.pop("details"),
                surgery=cli.registered_surgery)
        return super_init
