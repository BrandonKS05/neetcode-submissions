class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for amount in coins:
                if amount <= i:
                    dp[i] = min(dp[i - amount] + 1, dp[i])
        if dp[len(dp) - 1] == float("inf"):
            return -1
        else:
            return dp[len(dp) - 1]
        