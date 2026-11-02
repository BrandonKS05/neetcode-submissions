class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        start_idx = 0 
        total = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                start_idx = i + 1
                total = 0
        return start_idx

            

        