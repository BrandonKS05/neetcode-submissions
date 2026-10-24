class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        state = [0] * numCourses
        graph = [[] for __ in range(numCourses)]
        for i, j in prerequisites:
            graph[j].append(i)
        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            state[node] = 1
            for neighbors in graph[node]:
                if not dfs(neighbors):
                    return False
            state[node] = 2
            return True
        for r in range(numCourses):
            if not dfs(r):
                return False
        return True

            

            

         