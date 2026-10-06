from faker import Faker


def create_person():
    fake = Faker()

    return {
        "name": fake.name(),
        "email": fake.email()
    }