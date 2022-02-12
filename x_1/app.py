from math import factorial


class Phone:
    def __init__(self, price, camera_count, screen_size):
        self.price = price
        self.camera_count = camera_count
        self.screen_size = screen_size


class TaiwanPhone(Phone):
    def special_freature(self, n):
        if not isinstance(n, int) or n <= 0:
            return 'Invalid input'

        dp = [1] * n
        if n > 2:
            for i in range(2, n):
                dp[i] = dp[i-1] + dp[i-2]
            s = str(dp[-1])
            x = int(s[-2])
            y = int(s[-1])
            try:
                return int(factorial(x)/factorial(x-y))
            except ValueError:
                raise Exception('Invalid Set/Sub-set number')
        elif n > 0:
            return 1


class GooglePhone(Phone):
    def special_freature(self, int_list: list) -> list:
        return sorted(filter(lambda x: x > 10 and x % 2 == 0, int_list), reverse=True)
