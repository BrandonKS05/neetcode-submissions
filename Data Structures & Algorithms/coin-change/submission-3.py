class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        length = amount + 1
        dp = [float('inf')] * length
        dp[0] = 0
        for i in range(1, length):
            for amount in coins:
                if amount <= i:
                    dp[i] = min(dp[i - amount] + 1, dp[i])
        if dp[length - 1] == float("inf"):
            return -1
        else:
            return dp[length - 1]
        