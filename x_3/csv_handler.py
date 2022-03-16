import os
import sys

from random import choice, choices
from string import ascii_letters


class CsvHandler(object):
    
    letters = list(ascii_letters)
    numbers = [str(i) for i in range(10)]
    names   = [
        'Walker',
        'White',
        'Murray',
        'Johnson',
        'Vassell',
        'Collins',
        'Poeltl',
        'Richardson',
        'Primo',
        'Landale'
    ]
    
    def __init__(self):
        if 'ilovecoffee' not in os.listdir():
            os.mkdir('./ilovecoffee')
        self.file = os.path.join(os.getcwd(), 'ilovecoffee', 'customers.csv')
    
    def calculate_csv(self):
        customers = self.get_customers()
        if customers:
            ids, names, phones, frequencies = zip(*customers)
            frequencies = [int(f) for f in frequencies]
            median      = self.calculate_median(frequencies)
            mode        = self.calculate_mode(frequencies)
            average     = self.calculate_average(frequencies)
            print(f'Median : {median}')
            print(f'Mode   : {mode}')
            print(f'Average: {average:.5f}')
        else:
            print('No customers data')
        return
    
    def create_csv(self):
        """
        題目沒有說明customers.csv是追加or覆蓋
        這邊使用追加
        """
        frequency_choices = [i for i in range(21)]
        # get existing customers
        existing_customers = self.get_customers()
        if existing_customers:
            existing_ids, names, existing_phones, frequencies = zip(*existing_customers)
            existing_ids    = list(existing_ids)
            existing_phones = list(existing_phones)
        else:
            existing_ids    = list()
            existing_phones = list()
            
        for i in range(500):
            # create customer
            id_repeat      = True
            phone_repeat   = True
            customer_id    = ''
            customer_phone = ''
            while id_repeat:
                customer_id = self.create_id()
                if customer_id not in existing_ids:
                    id_repeat = False
                # else:
                #     print(f'ID repeat: {customer_id}')
            while phone_repeat:
                customer_phone = self.create_phone()
                if customer_phone not in existing_phones:
                    phone_repeat = False
                # else:
                #     print(f'Phone repeat: {customer_phone}')
            customer_name      = choice(self.names)
            customer_name      = f'{customer_name}.{customer_id}'
            customer_frequency = choice(frequency_choices)
            # write data
            with open(self.file, 'a', newline='') as csv:
                csv.write(f'"{customer_id}", "{customer_name}", "{customer_phone}", "{customer_frequency}"\n')
            existing_ids.append(customer_id)
            existing_phones.append(customer_phone)
        return
    
    def create_id(self):
        head = choice(self.letters)
        body = ''.join(choices(self.letters + self.numbers, k=7))
        return head + body
    
    def create_phone(self):
        output = '+8869' + ''.join(choices(self.numbers, k=8))
        return output
    
    def get_customers(self):
        csv_header = 'customer_id, customer_name, customer_mobile, frequency\n'
        output     = list()
        if 'customers.csv' in os.listdir('./ilovecoffee'):            
            with open(self.file, 'r+', newline='') as csv:
                for row in csv:
                    temp_row = row.replace('"', '')
                    temp_row = temp_row.replace('\n', '')
                    # print(temp_row)
                    output.append(temp_row.split(', '))
                if not output:
                    csv.write(csv_header)
        else:
            with open(self.file, 'w', newline='') as csv:
                csv.write(csv_header)
        # pop header
        if output:
            output.pop(0)
        return output
    
    def check_repeat(self):
        repeat = False
        customers = self.get_customers()
        if customers:
            ids, names, phones, frequencies = zip(*customers)
            id_set    = set(ids)
            phone_set = set(phones)
            if len(ids) != len(id_set):
                print('Some ids repeat')
                repeat = True
            if len(phones) != len(phone_set):
                print('Some ids repeat')
                repeat = True
        if not repeat:
            print('No id & phone repeat')
        return repeat
    
    def calculate_median(self, data: list):
        if not data:
            return None
        data.sort()
        count = len(data)
        if count % 2 == 0:
            ind0 = int(count / 2)
            ind1 = ind0 - 1
            return (data[ind0] + data[ind1]) / 2
        else:
            ind = int((count - 1) / 2)
            return data[ind]
        
    def calculate_mode(self, data: list):
        if not data:
            return None
        output     = list()
        statistics = dict()
        for i in set(data):
            statistics[i] = data.count(i)
        max_count = max(statistics.values())
        for k, v in statistics.items():
            if v == max_count:
                output.append(k)
        return output
    
    def calculate_average(self, data: list):
        if not data:
            return None
        return sum(data) / len(data)


if __name__ == '__main__':
    
    handler = CsvHandler()
    test_data = [1, 2, 2, 3, 5, 6, 7, 8, 9, 9]
    
    if len(sys.argv) == 1:
        handler.create_csv()
        
    else:
        if sys.argv[1] == 'calculate_csv':
            handler.calculate_csv()
        if sys.argv[1] == 'create_id':
            print(handler.create_id())
        elif sys.argv[1] == 'create_phone':
            print(handler.create_phone())
        elif sys.argv[1] == 'get_customers':
            data = handler.get_customers()
            for d in data:
                print(d)
        elif sys.argv[1] == 'check_repeat':
            handler.check_repeat()
        elif sys.argv[1] == 'calculate_median':
            print(handler.calculate_median(test_data))
        elif sys.argv[1] == 'calculate_mode':
            print(handler.calculate_mode(test_data))
        elif sys.argv[1] == 'calculate_average':
            print(handler.calculate_average(test_data))
