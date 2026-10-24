class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        best = 0
        for i in range(n):
            if i < n - 1 and prices[i] < prices[i+1]:
                y = prices[i]
                j = i
                while j < n:
                    profit = prices[j] - y
                    best = max(best, profit)
                    j+=1
        return best
            
