class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        candidate = 0
        best = 0
        for current in range(1, len(prices)):
            cur_profit = prices[current] - prices[candidate]
            if prices[current] < prices[candidate]:
                candidate = current
            
            best = max(best, cur_profit)
        return best

        