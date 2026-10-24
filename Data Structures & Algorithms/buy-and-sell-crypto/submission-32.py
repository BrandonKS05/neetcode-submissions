class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0 
        best = 0
        for sell in range(1, len(prices)):
            if prices[sell]<prices[buy]:
                buy = sell
            best = max(best, prices[sell]-prices[buy])
        return best

    
            


        
            


