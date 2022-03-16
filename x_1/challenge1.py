from math import factorial
import abc


class Phone(abc.ABC):
    __price = None
    __camera_count = None
    __screen_size = None

    @property
    @abc.abstractmethod
    def price(self):
        return self.__price

    @property
    @abc.abstractmethod
    def camera_count(self):
        return self.__camera_count

    @property
    @abc.abstractmethod
    def screen_size(self):
        return self.__screen_size

    @abc.abstractmethod
    def special_freature():
        pass


class GooglePhone(Phone):
    def __init__(self):
        self.__price = 10
        self.__camera_count = 3
        self.__screen_size = 5

    @property
    def price(self):
        return self.__price

    @property
    def camera_count(self):
        return self.__camera_count

    @property
    def screen_size(self):
        return self.__screen_size

    def special_freature(self) -> list:
        print("Usage: 3 43 62 15 18 22")
        input_string = input('Enter elements of a list separated by space:\n')
        input_list = [int(unit) for unit in input_string.split()]
        return sorted([unit for unit in input_list if unit > 10 and unit % 2 == 0], reverse=True)


class TaiwanPhone(Phone):
    def __init__(self):
        self.__price = 20
        self.__camera_count = 1
        self.__screen_size = 3

    @property
    def price(self):
        return self.__price

    @property
    def camera_count(self):
        return self.__camera_count

    @property
    def screen_size(self):
        return self.__screen_size

    def special_freature(self) -> int:
        number = int(input('Enter elements: '))
        if number <= 0:
            raise ValueError("Should be a positive number~")

        def fibonacci(number):
            x, y = 0, 1
            while(number):
                x, y, number = y, x+y, number-1
            return x
        x = fibonacci(number)
        return factorial(int((x % 100)/10))//factorial(int((x % 100)/10)-int(x % 10))


if __name__ == '__main__':

    phone1 = GooglePhone()
    print(phone1.special_freature())

    phone2 = TaiwanPhone()
    print(phone2.special_freature())
