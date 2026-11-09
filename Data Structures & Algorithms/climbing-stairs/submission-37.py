from functools import cache
class Solution:
    @cache
    def climbStairs(self, n: int) -> int: return n if n < 3 else self.climbStairs(n-1) + self.climbStairs(n-2)