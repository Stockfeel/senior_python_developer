import abc
import heapq

FIBONACCI_LOOKUP = dict()


def fibonacci(number):
    if number == 0:
        return 0
    elif number in {1, 2}:
        return 1
    elif FIBONACCI_LOOKUP.get(number):
        return FIBONACCI_LOOKUP[number]
    else:
        FIBONACCI_LOOKUP[number] = fibonacci(number-1) + fibonacci(number-2)
        return FIBONACCI_LOOKUP[number]


class Phone(metaclass=abc.ABCMeta):
    def __init__(self, price, camera_count, screen_size):
        self.price = price
        self.camera_count = camera_count
        self.screen_size = screen_size

    # maybe freature is a misspelling
    @abc.abstractmethod
    def special_freature(self):
        return NotImplemented


class GooglePhone(Phone):

    def special_freature(self, elements):
        ans = []

        for element in elements:
            if element > 10 and element % 2 == 0:
                heapq.heappush(ans, element)

        return ans


class TaiwanPhone(Phone):

    def special_freature(self, number):
        ans = 1
        fib_ans = fibonacci(number)

        last_one_num = fib_ans % 10
        fib_ans //= 10
        second_last_num = fib_ans // 10 % 10

        if second_last_num < last_one_num:
            raise ValueError(
                "Second Last number must be larger than the last one"
            )

        if last_one_num != 0:
            for num in range(second_last_num, last_one_num, -1):
                ans *= num

        return ans
