from typing import List

class GooglePhone():
    def __init__(self) -> None:
        self.price = 10
        self.camera_count = 3
        self.screen_size = 5

    def sp_feature(self, nums: List):
        ans = []
        for num in nums:
            if num%2 == 0:
                ans.append(num)
        return sorted(ans, reverse=True)

if __name__ == '__main__':
    sample = [1,2,3,6,13,50,100]
    obj = GooglePhone()
    ans = obj.sp_feature(sample)
    print(ans)