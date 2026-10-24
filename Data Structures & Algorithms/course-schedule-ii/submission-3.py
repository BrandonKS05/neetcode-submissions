class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        
        for parent, child in prerequisites:
            adj[parent].append(child)
        
        res = []

        undiscovered, discovered, processed = 0, 1, 2
        state = [undiscovered] * numCourses

        def dfs(start):
            if state[start] == discovered:
                return False
            if state[start] == processed:
                return True
            
            state[start] = discovered
            for neighbor in adj[start]:
                if not dfs(neighbor):
                    return False

            state[start] = processed
            res.append(start)
            
            return True
            
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
            


        