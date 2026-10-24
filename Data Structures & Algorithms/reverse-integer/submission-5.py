class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
    
        while x != 0:
            last = x % 10
            x = x // 10

            if res > INT_MAX // 10 or (res == INT_MAX and last > INT_MAX % 10):
                return 0

            res = res * 10
            res += last
        
        return res * sign

     
        