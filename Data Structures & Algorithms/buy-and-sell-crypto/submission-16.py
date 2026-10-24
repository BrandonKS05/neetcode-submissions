class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        j=0
        for i in range(1,len(prices)):
            if prices[i] < prices[j]:
                j=i
            if prices[i]-prices[j]>profit:
                profit = prices[i]-prices[j]
        return profit
            


        
            


