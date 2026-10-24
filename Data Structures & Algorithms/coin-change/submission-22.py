class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount
        for i in range(1, amount + 1):
            for num in coins:
                dp[i] = min(dp[i - num] + 1, dp[i]) if num <= i else dp[i]
        return dp[amount] if dp[amount] != amount + 1 else -1