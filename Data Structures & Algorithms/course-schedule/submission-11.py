class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
        
        
        completed = 0
        visit = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                visit.append(i)
                

        while(visit):
            start = visit.popleft()
            completed += 1
            for neighbor in adj[start]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    visit.append(neighbor)

        return completed == numCourses

