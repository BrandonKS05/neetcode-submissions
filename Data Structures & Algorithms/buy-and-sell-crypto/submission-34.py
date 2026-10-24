class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        candidate = 0
        best_profit = 0
        for current_date in range(1, len(prices)):
            current_profit = prices[current_date] - prices[candidate]
            if prices[current_date] < prices[candidate]:
                candidate = current_date
            
            best_profit = max(best_profit, current_profit)
        return best_profit

        