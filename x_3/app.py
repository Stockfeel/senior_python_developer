from pathlib import Path
import csv
import os
import random
import string
from faker import Faker
from faker.providers.phone_number.zh_TW import Provider
import phonenumbers
import statistics


class PhoneNumberProvider(Provider):
    def tw_phone_number(self):
        return f'+886 {self.msisdn()[4:]}'


class CsvHandler():

    def __init__(self):
        self.cwd = os.getcwd()
        Path(f"{self.cwd}/ilovecoffee").mkdir(parents=True, exist_ok=True)

    def create_csv(self):
        header = ['customer_id', 'customer_name',
                  'customer_mobile', 'frequency']
        names = ['jane', 'jimmy', 'leon', 'alex', 'cindy',
                 'wendy', 'evelyn', 'mia', 'sean', 'david']
        fake = Faker()
        fake.add_provider(PhoneNumberProvider)
        with open(f'{self.cwd}/ilovecoffee/customers', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            phones = set()
            for _ in range(500):
                chars = ''.join(random.choices(string.ascii_letters, k=4))
                nums = ''.join(random.choices(string.digits, k=4))
                phone = fake.tw_phone_number()
                my_number = phonenumbers.parse(phone, "TW")
                while phone in phones or not phonenumbers.is_valid_number(my_number):
                    phone = fake.tw_phone_number()
                    my_number = phonenumbers.parse(phone, "TW")

                phones.add(phone)
                customer_id = f'{chars}{nums}'
                name = f'{random.choice(names)}.{customer_id}'
                frequency = random.randint(0, 20)
                data = [customer_id, name, phone, frequency]

                writer.writerow(data)

    def calculate_csv(self):
        with open(f'{self.cwd}/ilovecoffee/customers', newline='') as csvfile:

            rows = csv.reader(csvfile)

            frequencies = []

            for i, row in enumerate(rows):
                if i == 0:
                    continue
                frequencies.append(int(row[-1]))

            stat = statistics.median(frequencies)
            mode = statistics.mode(frequencies)
            average = round(statistics.mean(frequencies), 5)
            print(stat, mode, average)


if __name__ == "__main__":
    c = CsvHandler()
    c.create_csv()
    c.calculate_csv()
