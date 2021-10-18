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
        return f'{self.name} {self.company} {self.position} {self.email}'


# dodac funkcje z modułu

person_1 = Card(name=fake.name(), surrname=fake.name(), company=fake.company(), position=fake.job(), email=fake.email())
person_2 = Card(name=fake.name(), surrname=fake.name(), company=fake.company(), position=fake.job(), email=fake.email())
person_3 = Card(name=fake.name(), surrname=fake.name(), company=fake.company(), position=fake.job(), email=fake.email())
person_4 = Card(name=fake.name(), surrname=fake.name(), company=fake.company(), position=fake.job(), email=fake.email())
person_5 = Card(name=fake.name(), surrname=fake.name(), company=fake.company(), position=fake.job(), email=fake.email())


print(person_1.name, person_1.company, person_1.position, person_1.email)
print(person_2)