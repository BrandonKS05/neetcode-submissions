class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        best = max(piles)
    
        
        def check(num):
            count = 0
            for banana in piles:
                result = math.ceil(banana / num)
                count += result
            return count

        l = 1
        r = best
        while l <= r:
            mid = (l + r) // 2
            candidate = check(mid)
          

            if candidate <= h:
                best = min(best, mid)
                r = mid - 1
            elif candidate > h:
                l = mid + 1
        return best
            
