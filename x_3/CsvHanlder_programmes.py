import os
import string
import random
import numpy as np
import pandas as pd
from tabulate import tabulate
from typing import List

class CsvHanlder():
    def __init__(self) -> None:
        self.folder_name = '\\ilovecoffee'
        self.csv_name = self.folder_name+'\\customers.csv'
        self.columns_name = ['customer_id', 'customer_name', 'customer_mobile', 'frequency']
        self.counts = 500

        self.nums = [i for i in range(10)]
        self.capitals = [i for i in string.ascii_uppercase]
        self.lowercase = [i for i in string.ascii_lowercase]
        self.names = ['Alen', 'Alex', 'Bonny', 'Cathay', 'Cheryl', 'Elva', 'Georgie', 'Ian', 'Janey', 'Kevin']

        self.customer_id_List = []
        self.customer_name_List = []
        self.customer_mobile_list = []
        self.frequency_List = []

        self.customersCSV = pd.DataFrame()

        self.setup()

    # Check folder exists or not
    def setup(self):
        if not(os.path.isdir(os.getcwd()+self.folder_name)):
            os.mkdir(os.getcwd()+self.folder_name)
    
    def create_customer_id(self) -> List[str]:
        first_id = np.random.choice(self.capitals+self.lowercase, size=(self.counts,1), replace=True)
        other_id = np.random.choice(self.nums+self.capitals+self.lowercase, size=(self.counts,7), replace=True)
        total_id = np.append(first_id, other_id, axis=1)
        str_contact = ''
        return [str_contact.join(i) for i in total_id]
        
    def create_customer_name(self, customer_id: List[str]) -> List[str]:
        names_array = np.random.choice(self.names, size=(self.counts,1), replace=True)
        total_names_array = np.append(names_array, np.array(customer_id).reshape(self.counts,1), axis=1)
        str_contact = '.'
        return [str_contact.join(i) for i in total_names_array]

    def create_customer_mobile(self, counts: int) -> List[str]:
        phone_title = ['+8869' for i in range(counts)]
        phone_title = np.array(phone_title).reshape(counts,1)
        phone_number = np.random.choice(self.nums, size=(counts,8), replace=True)
        total_phone_number = np.append(np.array(phone_title).reshape(counts,1), phone_number, axis=1)
        str_contact = ''
        return [str_contact.join(i) for i in total_phone_number]

    def check_customer_mobile_duplicate(self, phone_number_List: List[str]) -> bool:
        return True if len(phone_number_List) != len(set(phone_number_List)) else False

    def create_customer_mobile_nonduplicate(self) -> List[str]:
        customer_mobile_List = self.create_customer_mobile(self.counts)
        
        while self.check_customer_mobile_duplicate(customer_mobile_List):
            customer_mobile_List = list(dict.fromkeys(customer_mobile_List))
            fullup_counts = self.counts - len(customer_mobile_List)
            fillup_mobile_List = self.create_customer_mobile(fullup_counts)
            customer_mobile_List += fillup_mobile_List
        return customer_mobile_List
    
    def create_feequency(self) -> List[str]:
        return [str(random.randint(0, 20)) for i in range(self.counts)]

    def create_csv(self):
        self.customer_id_List = self.create_customer_id()
        self.customer_name_List = self.create_customer_name(self.customer_id_List)
        self.customer_mobile_list = self.create_customer_mobile_nonduplicate()
        self.frequency_List = self.create_feequency()

        self.customersCSV = pd.DataFrame(list(zip(self.customer_id_List, self.customer_name_List,
        self.customer_mobile_list, self.frequency_List)), columns = self.columns_name)
        self.customersCSV.to_csv(os.getcwd()+self.csv_name, index=False, encoding='utf-8-sig')
    
    def calculate_csv(self):
        if not(os.path.isfile(os.getcwd()+self.csv_name)):
            print()
            print('You need to excute create_csv first')
        else:
            frequency_median = str(self.customersCSV['frequency'].astype('int').median())
            frequency_mode = self.customersCSV['frequency'].value_counts().index[0]
            frequency_mean = str(round(self.customersCSV['frequency'].astype('int').mean(), 5))

            table = [[frequency_median, frequency_mode, frequency_mean]]
            print(tabulate(table, headers=['中數','眾數','平均數']))

if __name__ == '__main__':
    x_3 = CsvHanlder()
    x_3.create_csv()
    x_3.calculate_csv()
