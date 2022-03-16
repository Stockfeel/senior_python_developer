# -*- coding: UTF-8 -*-
import csv
import os
from random import choice, choices
from string import ascii_letters, digits

import numpy as np


class CsvHanlder():
    def __init__(self):
        self.path, _ = os.path.split(os.path.abspath(__file__))
        # detect ilovecoffee folder is not exist
        if not os.path.isdir(f"{self.path}/ilovecoffee"):
            os.mkdir(f"{self.path}/ilovecoffee")
        # static english name
        self.name_list = ['tom', 'perer', 'andy',
                          'hank', 'bruce', 'bill',
                          'bob', 'bill', 'david',
                          'dave']

    def create_csv(self):
        """隨機寫入 500 筆客戶資料至 /ilovecoffee/customers.csv"""
        with open(f"{self.path}/ilovecoffee/customers.csv", 'w', newline='') as csvfile:
            # write header
            writer = csv.DictWriter(csvfile,
                                    fieldnames=['customer_id', 'customer_name',
                                                'customer_mobile', 'frequency'],
                                    delimiter=',')
            writer.writeheader()

            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL, delimiter=',')

            for _ in range(500):
                mobile_set = set()
                customer_id = f"{choice(ascii_letters)}{''.join(choices(ascii_letters+digits, k=7))}"
                customer_name = f"{choice(self.name_list)}.{customer_id}"

                while 1:
                    customer_mobile = f"+886{''.join(choices(digits, k=9))}"
                    if customer_mobile not in mobile_set:
                        mobile_set.add(customer_mobile)
                        break
                frequency = choice(range(21))
                writer.writerow([customer_id, customer_name,
                                 customer_mobile, frequency])

    def calculate_csv(self):
        """讀取 /ilovecoffee/customers.csv，並列印出 frequency 中數、眾數及平均數 (取至小數點後 5 位)"""
        with open(f"{self.path}/ilovecoffee/customers.csv", 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)

            # header
            _ = next(reader, None)

            nums = [int(i[3]) for i in reader]

        # Print answer
        print(f"Median:{np.median(nums)}")
        print(f"Mean:{round(np.mean(nums), 5)}")
        print(f"Mode(statistics):{np.argmax(np.bincount(nums))}")


if __name__ == '__main__':
    test_csv = CsvHanlder()
    test_csv.create_csv()
    test_csv.calculate_csv()
