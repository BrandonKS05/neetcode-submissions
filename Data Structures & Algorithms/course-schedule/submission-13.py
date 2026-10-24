class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]

        for parent, child in prerequisites:
            adj[child].append(parent)
          

        undiscovered, discovered, processed = 0, 1, 2
        state = [undiscovered] * numCourses
        
        def dfs(cur):
            if state[cur] == discovered:
                return False
            if state[cur] == processed:
                return True
            
            state[cur] = discovered

            for neighbor in adj[cur]:
                if not dfs(neighbor):
                    return False
            state[cur] = processed

            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True