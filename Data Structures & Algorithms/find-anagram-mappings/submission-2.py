class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        def findinx(a):
            for i in range(len(nums2)):
                if a == nums2[i]:
                    return i
        for num in nums1:
            res.append(findinx(num))
        return res
