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




person_1 = Card(name=fake.name(), surrname=fake.name(), company=fake.company(), position=fake.job(), email=fake.email())
person_2 = Card(name=fake.name(), surrname=fake.name(), company=fake.company(), position=fake.job(), email=fake.email())
person_3 = Card(name=fake.name(), surrname=fake.name(), company=fake.company(), position=fake.job(), email=fake.email())
person_4 = Card(name=fake.name(), surrname=fake.name(), company=fake.company(), position=fake.job(), email=fake.email())
person_5 = Card(name=fake.name(), surrname=fake.name(), company=fake.company(), position=fake.job(), email=fake.email())

person_list = [person_1, person_2, person_3, person_4, person_5]
card_list = []

Card.contact(person_1)

print(card_list)

# sortowanie
# 