class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [] #[-1, -1, 0, 1]
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            while l < r:
                newsolution = []
                if nums[i] + nums[l] + nums[r] == 0:
                    newsolution.append(nums[i])
                    newsolution.append(nums[l])
                    newsolution.append(nums[r])
                    result.append(newsolution)
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while r > l and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1 
        return result