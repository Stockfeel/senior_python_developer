import random
import string
import csv
from pathlib import Path
from collections import Counter
import statistics


class CsvHanlder():
    def __init__(self) -> None:
        self.target_path = Path("ilovecoffee")
        self.ensure_envir()

    def ensure_envir(self):
        if self.target_path.exists() and self.target_path.is_dir():
            print("found coffee!")
        else:
            print("not found coffee!")
            Path.mkdir(self.target_path)
            print("coffee created.")

    def get_random_custom_id(num: int):
        pass

    def generate_user_list(self, number):
        name_pool = ["tom", "roy", "hank", "alan", "bruce",
                     "cindy", "david", "elon", "fred", "george"]
        id_pool = "0123456789" + string.ascii_letters

        user_list = []
        for _ in range(number):
            customer_id = random.choice(string.ascii_letters)
            cellphone = "+8869"
            for _ in range(7):
                customer_id += random.choice(id_pool)
            for _ in range(8):
                cellphone += str(random.randint(0, 9))
            customer_name = name_pool[random.randint(0, 9)] + "." + customer_id
            frequency = random.randint(0, 20)
            # print(customer_id, customer_name, cellphone, frequency)
            user_list.append((customer_id, customer_name, cellphone, frequency))
        return user_list

    def create_csv(self):
        user_list = self.generate_user_list(500)
        with open(Path(self.target_path, "customers.csv"), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(["customer_id", "customer_name", "customer_mobile", "frequency"])
            for customer_id, customer_name, cellphone, frequency in user_list:
                writer.writerow([customer_id, customer_name, cellphone, frequency])

    def calculate_csv(self):
        with open(Path(self.target_path, "customers.csv"), newline='') as csvfile:
            rows = csv.reader(csvfile)
            next(rows, None)
            frequencies = []
            for row in rows:
                frequencies.append(int(row[3]))
        # print(frequencies)
        data = Counter(frequencies)
        back = 0
        # print(data.most_common())

        # mode numbers can more than one...
        for each_mode, times in data.most_common():
            if back > times:
                break
            print(f"mode: {each_mode}")
            back = times

        median = statistics.median(frequencies)
        print(f"median: {median}")
        mean = round(statistics.mean(frequencies), 5)
        print(f"mean: {mean}")


if __name__ == '__main__':
    obj = CsvHanlder()
    obj.create_csv()
    obj.calculate_csv()
