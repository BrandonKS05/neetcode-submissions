class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start, stack, total):
            if total == target:
                res.append(stack[:])
                return
            if total > target:
                return
            for i in range(start, len(nums)):
                stack.append(nums[i])
                backtrack(i, stack, total + nums[i])
                stack.pop()

        backtrack(0, [], 0)
        return res
        