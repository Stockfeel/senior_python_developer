import sys


class BasePhone(object):
    
    price        = 1
    camera_count = 1
    screen_size  = 1
    
    def special_freature(self):
        return None
    
    
class GooglePhone(BasePhone):
    
    def __init__(self):
        self.price        = 10
        self.camera_count = 3
        self.screen_size  = 5
        
    def special_freature(self, input: list):
        output = [i for i in input if i % 2 == 0 and i > 10]
        output.sort(reverse=True)
        return output
    
    
class TaiwanPhone(BasePhone):
    
    def __init__(self):
        self.price        = 20
        self.camera_count = 1
        self.screen_size  = 3
        
    def special_freature(self, i: int):
        """
        未說明
        1. 費式數列運算結果為個位數
        2. 費式數列運算結果之十位數小於個位數
        之處理方式，暫時定義：
        1. return 0
        2. return 十位數之階乘
        """
        fibo = TaiwanPhone.fibonacci(i)
        if fibo < 10:
            return 0
        fibo = str(fibo)
        x = int(fibo[-2])
        y = int(fibo[-1])
        if x < y:
            y = x
        output = 1
        for _ in range(y):
            output *= x
            x -= 1
        return output
    
    @staticmethod
    def fibonacci(i: int):
        if i < 1:
            return 0
        if i < 3:
            return 1
        else:
            return TaiwanPhone.fibonacci(i - 1) + TaiwanPhone.fibonacci(i - 2)
    
if __name__ == '__main__':
    
    if len(sys.argv) == 1:
        print('Please input phone name')
    else:
        test_data = {
            'google': [3, 43, 62, 15, 18, 22],
            'taiwan': 11
        }
        output    = None
        
        if sys.argv[1] == 'google':
            phone = GooglePhone()
            output = phone.special_freature(test_data['google'])
        elif sys.argv[1] == 'taiwan':
            phone = TaiwanPhone()
            output = phone.special_freature(test_data['taiwan'])
        elif sys.argv[1] == 'fibo':
            output = TaiwanPhone.fibonacci(test_data['taiwan'])
        
        print(output)
