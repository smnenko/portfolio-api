from random import randint, choice

from faker import Faker


class FakeHuman:

    FAKE = Faker()
    DIGITS = '123456789'
    SYMBOLS = '._-'
    RANDOM_DIGITS_COUNT = randint(5, 7)

    def __init__(self):
        self.first_name = self.FAKE.first_name()
        self.last_name = self.FAKE.last_name()

    @property
    def username(self):
        username = (
            f'{self.first_name.lower()}'
            f'{choice(self.SYMBOLS)}'
            f'{self.last_name.lower()}'
            f'{"".join([choice(self.DIGITS) for _ in range(self.RANDOM_DIGITS_COUNT - 2)])}'
        )
        return username if len(username) <= 32 else username[:32]

    @property
    def password(self):
        password = (
            f'{self.last_name}'
            f'{choice(self.DIGITS)}'
            f'{self.first_name}'
            f'{"".join([choice(self.DIGITS) for _ in range(self.RANDOM_DIGITS_COUNT)])}'
        )
        return password if len(password) <= 32 else password[:32]

    @property
    def secret_answer(self):
        return int(''.join(choice(self.DIGITS) for _ in range(4)))