class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        best = 0
        left = 0
        right = 0
        while right < n:
            if prices[right] < prices[left]:
                left = right
            profit = prices[right] - prices[left]
            best = max(best, profit)
            right += 1
        return best
            
