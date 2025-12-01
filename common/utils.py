from faker import Faker
from random import choice, randint
from string import ascii_letters, digits


Faker.seed(randint(1, 999999999))
fake = Faker()
fake.seed_instance(0)


def random_number(start: int = 1, end: int = 100) -> int:
    return randint(start, end)


def random_string(start: int = 1, end: int = 50) -> str:
    return ''.join(choice(ascii_letters + digits) for _ in range(randint(start, end)))


def random_list_of_strings(start: int = 9, end: int = 15) -> list[str]:
    return [random_string() for _ in range(randint(start, end))]
