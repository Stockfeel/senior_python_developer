from typing import List


class Phone():
    def __init__(self, price, camera_count, screen_size) -> None:
        self.price = price
        self.camera_count = camera_count
        self.screen_size = screen_size

class GooglePhone(Phone):
    def __init__(self, price=10, camera_count=3, screen_size=5) -> None:
        super().__init__(price, camera_count, screen_size)

    def sp_feature(self, nums: List):
        ans = []
        for num in nums:
            if num%2 == 0:
                ans.append(num)
        return sorted(ans, reverse=True)


class TaiwanPhone(Phone):
    def __init__(self, price=20, camera_count=1, screen_size=3) -> None:
        super().__init__(price, camera_count, screen_size)

    def fibonacci(self, the_n_th_number):
        lis = [1, 2]
        if the_n_th_number == 1:
            return lis[0]
        elif the_n_th_number == 2:
            return lis[1]
        else:
            loop_time = the_n_th_number - 2
            for _ in range(loop_time):
                ans = lis[-1] + lis[-2]
                lis.append(ans)
            # print(f"fibonacci list: {lis}")
            return ans

    def sp_feature(self, n: int):
        fib_num = self.fibonacci(n)
        # print(f"fib_num: {fib_num}")

        x = (fib_num // 10)%10
        y = fib_num % 10

        ans = 1
        if y == 0:
            return ans
        elif x > y:
            for num in range(x, y, -1):
                ans *= num
        else:
            # print("can't get answer because x < y...")
            ans = 0

        return ans




if __name__ == '__main__':
    sample = [1,2,3,6,13,50,100]
    obj = GooglePhone()
    ans = obj.sp_feature(sample)
    print(ans)

    the_n_th_number = 14
    obj2 = TaiwanPhone()
    ans = obj2.sp_feature(the_n_th_number)
    print(ans)
