class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        length = amount + 1
        dp, dp[0] = [length] * length, 0
        for i in range(1, length):
            for num in coins:
                dp[i] = min(dp[i - num] + 1, dp[i]) if num <= i else dp[i]
        return dp[amount] if dp[amount] != length else -1