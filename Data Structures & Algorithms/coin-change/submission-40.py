from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def d(t):
            c = float('inf')
            if t == amount:
                return 0

            for i in range(len(coins)):
                if t + coins[i] <= amount:
                    c = min(c, d(t + coins[i]) + 1)

            return c
        x = d(0)

        return -1 if x == float('inf') else x