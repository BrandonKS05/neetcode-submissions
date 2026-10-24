class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 0
        times = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
        print(times)
        queue = []
        heapq.heappush(queue, (grid[0][0], 0, 0))
        while queue:
            ti, y, x = heapq.heappop(queue)
            if x == len(grid[0]) - 1 and y == len(grid) - 1:
                break
            for yi, xi in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                yf = y + yi
                xf = x + xi
                if xf < 0 or yf < 0 or xf >= len(grid[0]) or yf >= len(grid):
                    continue
                tf = max(ti, grid[yf][xf])
                
                if tf < times[yf][xf]:
                    times[yf][xf] = tf
                    heapq.heappush(queue, (tf, yf, xf))

        return ti
        