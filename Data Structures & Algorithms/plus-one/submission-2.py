class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        deq = deque(digits)
        n = len(deq) - 1
        deq[n] += 1
        if deq[n] == 10:
            r = n
            while r >= 0 and deq[r] >= 9:
                deq[r] = 0
                r -= 1
            if r ==-1:
                deq.appendleft(1)
            else:
                deq[r] = deq[r] + 1
        return list(deq)