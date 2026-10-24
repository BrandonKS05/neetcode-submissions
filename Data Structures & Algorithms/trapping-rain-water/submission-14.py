class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
       
        l = 0
        r = len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        while l <= r:
            if maxLeft <= maxRight:
                water = maxLeft - height[l]
                water = 0 if water < 0 else water
                res += water
                maxLeft = max(maxLeft, height[l])
                l += 1
            else:
                water = maxRight - height[r]
                water = 0 if water < 0 else water
                res += water
                maxRight = max(maxRight, height[r])
                r -= 1
        
        return res



        