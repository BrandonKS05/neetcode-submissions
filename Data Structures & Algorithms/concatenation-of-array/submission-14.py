class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newlist = []
        for num in nums:
            newlist.append(num)
        for newnums in nums:
            newlist.append(newnums)
        return newlist