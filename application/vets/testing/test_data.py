from vets.models import Address, Pet


class VetsTestData(object):
    """
    Just the area for the static data which are used in tests.
    """

    AUTH_GROUPS = [
        'vets',
        'clients',
        'receptionists',
        'vets-admin',
        'area-manager'
    ]

    SURGERIES = [
        {
            "surgery_name": "Oak",
            "address_line_1": "1 Darwin Way",
            "address_line_2": "Shrewsbury Business Park",
            "address_line_3": "Shrewsbury",
            "address_line_4": "",
            "post_code": "SY3 2WK",
            "org_area": Address.SY,
            "opening_time": "09:00:00",
            "closing_time": "17:30:00"
        },
        {
            "surgery_name": "Beech",
            "address_line_1": "345 Churchill Avenue",
            "address_line_2": "Leighton Business Park",
            "address_line_3": "Harmer hill",
            "address_line_4": "",
            "post_code": "SY4 5TU",
            "org_area": Address.SY,
            "opening_time": "08:00:00",
            "closing_time": "16:45:00"
        },
        {
            "surgery_name": "Maple",
            "address_line_1": "3 Green Street",
            "address_line_2": "Whitchurch",
            "address_line_3": "",
            "address_line_4": "",
            "post_code": "SY12 0WK",
            "org_area": Address.SY,
            "opening_time": "08:30:00",
            "closing_time": "17:00:00"
        },
        {
            "surgery_name": "Meranti",
            "address_line_1": "67 High Street",
            "address_line_2": "Chester",
            "address_line_3": "",
            "address_line_4": "",
            "post_code": "SCH1 2WK",
            "org_area": Address.CH,
            "opening_time": "10:00:00",
            "closing_time": "18:00:00"
        }
    ]

    CLIENTS = [
        {
            "client_username": "client1",
            "registered_surgery": "Oak",
            "address_line_1": "45 Springfields",
            "address_line_2": "Shrewsbury",
            "address_line_3": "",
            "address_line_4": "",
            "post_code": "SY1 3SD",
            "org_area": Address.SY
        },
        {
            "client_username": "client2",
            "registered_surgery": "Beech",
            "address_line_1": "34 Duffy Street",
            "address_line_2": "Hadnall",
            "address_line_3": "Shropshire",
            "address_line_4": "",
            "post_code": "SY3 2FG",
            "org_area": Address.SY
        },
        {
            "client_username": "client3",
            "registered_surgery": "Meranti",
            "address_line_1": "Flat 108",
            "address_line_2": "Kelsy Tower",
            "address_line_3": "Manchester",
            "address_line_4": "",
            "post_code": "M1 4FR",
            "org_area": Address.GM
        }
    ]

    VETS = [
        {
            "vet_username": "vet1",
            "base_surgery": "Oak",
            "address_line_1": "45 Le Cul De Sac",
            "address_line_2": "Wem",
            "address_line_3": "Shropshire",
            "address_line_4": "",
            "post_code": "SY4 5FK",
            "org_area": Address.SY,
            "salary": 50000
        },
        {
            "vet_username": "vet2",
            "base_surgery": "Meranti",
            "address_line_1": "122 Diagon Alley",
            "address_line_2": "Marchamley",
            "address_line_3": "",
            "address_line_4": "",
            "post_code": "CH5 3DF",
            "org_area": Address.CH,
            "salary": 45000
        },
        {
            "vet_username": "vet3",
            "base_surgery": "Beech",
            "address_line_1": "45 Some Street",
            "address_line_2": "Im tired of inputting",
            "address_line_3": "Test",
            "address_line_4": "Data",
            "post_code": "CH3 6FG",
            "org_area": Address.CH,
            "salary": 55000
        },
        {
            "vet_username": "vet4",
            "base_surgery": "Maple",
            "address_line_1": "66 High Street",
            "address_line_2": "Hodnet",
            "address_line_3": "Shrewsbury",
            "address_line_4": "",
            "post_code": "SY6 7HK",
            "org_area": Address.GM,
            "salary": 55600
        }
    ]

    PETS = [
        {
            "name": "Barbara",
            "species": Pet.DOG,
            "owner": "client1",
            "dob": "2022-01-01 09:00:00.000Z"
        },
        {
            "name": "Johnny",
            "species": Pet.CAT,
            "owner": "client1",
            "dob": "2021-04-05 09:00:00.000Z"
        },
        {
            "name": "Rudy",
            "species": Pet.HORSE,
            "owner": "client1",
            "dob": "2020-01-01 09:00:00.000Z"
        },
        {
            "name": "Simon",
            "species": Pet.DOG,
            "owner": "client1",
            "dob": "2022-01-01 09:00:00.000Z"
        },
        {
            "name": "Morty",
            "species": Pet.CAT,
            "owner": "client2",
            "dob": "2022-01-01 09:00:00.000Z"
        },
        {
            "name": "Rick",
            "species": Pet.DOG,
            "owner": "client2",
            "dob": "2022-01-01 09:00:00.000Z"
        },
        {
            "name": "Mike",
            "species": Pet.DOG,
            "owner": "client2",
            "dob": "2022-01-01 09:00:00.000Z"
        },
        {
            "name": "Dick",
            "species": Pet.DOG,
            "owner": "client3",
            "dob": "2022-01-01 09:00:00.000Z"
        },
        {
            "name": "Harry",
            "species": Pet.DOG,
            "owner": "client3",
            "dob": "2022-01-01 09:00:00.000Z"
        },
        {
            "name": "Tom",
            "species": Pet.DOG,
            "owner": "client3",
            "dob": "2020-01-01 09:00:00.000Z"
        }
    ]

    APPOINTMENTS = [
        {
            "appointment_date_time": "2023-03-23 11:00:00.000Z",
            "surgery": "Oak",
            "vet": "vet1",
            "pet": "Barbara",
            "client": "client1",
            "details": "Basic Checkup"
        }
    ]
