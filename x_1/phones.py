from typing import List

class phones():
    def __init__(self, price: int, camera_count: int, screen_size: int):
        self.price = price
        self.camera_count = camera_count
        self.screen_size = screen_size
        
class google_phone(phones):
    def __init__(self):
        super().__init__(price=10, camera_count=3, screen_size=5)
    
    def special_freature(self, arr: List[int]) -> List[int]:
        return sorted([i for i in arr if (i%2==0) and i>10], reverse=True)

class taiwan_phone(phones):
    def __init__(self):
        super().__init__(price=20, camera_count=1, screen_size=3)
    
    def fibonacci(self, num: int) -> int:
        return num if num < 2 else self.fibonacci(num - 2) + self.fibonacci(num - 1)

    def permutation(self, x: int, y: int) -> int:
        return 1 if (y == 0) else x * self.permutation(x-1, y-1)

    def special_freature(self, num: int) -> int:
        fibonacci_num = self.fibonacci(num)
        x = int((fibonacci_num % 100) / 10)
        y = fibonacci_num % 10
        return self.permutation(x, y) if (x >= y) else 0
