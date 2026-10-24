class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        res = water = 0
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        while (left <= right):
            if maxLeft <= maxRight:
                water = maxLeft - height[left]
                water = 0 if water < 0 else water
                res += water
                maxLeft = max(maxLeft, height[left])
                left += 1
            else: 
                water = maxRight - height[right]
                water = 0 if water < 0 else water
                res += water
                maxRight = max(maxRight, height[right])
                right -= 1
        return res
                


    