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
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
    def contact(self):
        return f"Wybieram numer {self.phone_number} i dzwonię do {self.name}"


class BusinessContact(BaseContact):
    def __init__(self, position, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.business_phone = business_phone
    def contact(self):
        return f"Wybieram numer {self.business_phone} i dzwonię do {self.name}"


person_2 = BaseContact(name=fake.name(), phone_number=fake.phone_number(), email=fake.email())
person_3 = BusinessContact(name=fake.name(), phone_number=fake.phone_number(), email=fake.email(), position=fake.job(), company=fake.company(), business_phone=fake.phone_number())

contact(person_2)