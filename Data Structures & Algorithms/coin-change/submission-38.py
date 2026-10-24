from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def d(t):
            c_ = float('inf')
            if t == amount:
                return 0

            for i in range(len(coins)):
                if coins[i] > amount or t > amount:
                    continue
                c_ = min(c_, d(t + coins[i]) + 1)

            return c_
        x = d(0)

        return -1 if x == float('inf') else x