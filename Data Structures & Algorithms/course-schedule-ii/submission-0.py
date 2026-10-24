class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        sol = []
        adj = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
        
        
        visit = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                visit.append(i)
                

        while(visit):
            start = visit.popleft()
            sol.append(start)
            for neighbor in adj[start]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    visit.append(neighbor)

        return [] if len(sol) != numCourses else sol
