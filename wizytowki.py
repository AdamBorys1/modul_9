from faker import Faker

fake = Faker()

class Card:
    def __init__(self, name, surrname, company, position, email):
        self.name = name
        self.surrname = surrname
        self.company = company
        self.position = position
        self.email = email

    def __str__(self):
        return f'{self.name} {self.email}'

    def contact(self):
        print(f"Kontaktuje się z {self.name}, {self.position}, {self.email}")

    @property
    def name_length(self):
        return (len(self.name) - 1)


person_1 = Card(name=fake.name(), surrname=fake.name(), company=fake.company(), position=fake.job(), email=fake.email())




class BaseContact:
    def __init__(self, name, surrname, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.surrname = surrname
    def contact(self):
        print(f"Wybieram numer {self.phone_number} i dzwonię do {self.name} {self.surrname}")
    @property
    def label_length(self):
        return (len(self.name) - 1)


class BusinessContact(BaseContact):
    def __init__(self, position, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.business_phone = business_phone
    def contact(self):
        print(f"Wybieram numer {self.business_phone} i dzwonię do {self.name}")
    @property
    def label_length(self):
        return (len(self.name) - 1)



person_2 = BaseContact(name="Arek", surrname="Trzeciński", phone_number="634829517", email="a.trze@wp.pl")
person_3 = BusinessContact(name="Arek", surrname="Trzeciński", phone_number="634829517", email="a.trze@wp.pl", position="kierownik", company="Genomed", business_phone="836027674")

BaseContact.contact(person_2)