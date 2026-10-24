class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        length = amount + 1
        dp = [float('inf')] * length
        dp[0] = 0
        for i in range(1, length):
            for num in coins:
                if num <= i:
                    dp[i] = min(dp[i - num] + 1, dp[i])
        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]
        