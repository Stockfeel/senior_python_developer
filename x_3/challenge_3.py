#!/usr/bin/env python3

import csv
import os
import random
import string

NUMBERS = '0123456789'

LETTERS = string.ascii_letters

WORDS = NUMBERS + LETTERS

ENGLISHNAMES = [
    'james', 'percy', 'tim', 'tom', 'eve', 'eden', 'willy',
    'kevin', 'vivian', 'may'
]
PHONES = set()

FOLDER = 'ilovecoffee'


class CsvHandler:

    @staticmethod
    def file_dir():
        return f"{os.path.dirname(os.path.abspath(__file__))}/{FOLDER}"

    def __init__(self):
        if not os.path.exists(self.file_dir()):
            os.mkdir(self.file_dir())
        self.create_csv()

    def create_csv(self):

        with open(f"{self.file_dir()}/customers.csv", 'w',
                  newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                ['cusotmer_id', 'customer_name',
                 'customer_mobile', 'frequency']
            )

            for i in range(500):
                customer_id = self.random_customer_id()
                customer_name = self.random_customer_name(customer_id)
                customer_mobile = self.random_customer_mobile()
                frequency = self.random_frequency()
                writer.writerow(
                    [customer_id, customer_name, customer_mobile, frequency]
                )

    def random_customer_id(self):
        return ''.join(random.choice(LETTERS) for i in range(1)) + \
            ''.join(random.choice(WORDS) for i in range(5))

    def random_customer_name(self, customer_id):
        return f"{random.choice(ENGLISHNAMES)}.{customer_id}"

    def random_customer_mobile(self):
        new_phone = ''.join(random.choice(NUMBERS) for i in range(9))
        while new_phone in PHONES:
            new_phone = ''.join(random.choice(NUMBERS) for i in range(9))

        PHONES.add(new_phone)
        return f"+886{new_phone}"

    def random_frequency(self):
        return str(random.randrange(0, 21))
