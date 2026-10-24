class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.stack = []
        self.k = k
        for num in nums:
            heapq.heappush(self.stack, num)
            if len(self.stack) > k:
                heapq.heappop(self.stack)

    def add(self, val: int) -> int:
        heapq.heappush(self.stack, val)
        if len(self.stack) > self.k:
                heapq.heappop(self.stack)
        return self.stack[0]
        
        
