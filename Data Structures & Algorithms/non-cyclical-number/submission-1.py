class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def calculate(n):
            if n == 1:
                return True
            elif n in seen:
                return False
            seen.add(n)
            total = 0
            while n > 0:
                d = n % 10
                d = d * d
                total += d
                n = n // 10
            return calculate(total)
        return calculate(n)
