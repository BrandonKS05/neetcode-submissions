class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        for neighbor, me in prerequisites:
            if me not in graph:
                graph[me] = []
            graph[me].append(neighbor)
            in_degree[neighbor] += 1
        print(graph)

        queue = deque()
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)

        completed = 0
        while queue:
            me = queue.popleft()
            completed += 1
            for neighbor in graph[me]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return completed == numCourses




       
     
        