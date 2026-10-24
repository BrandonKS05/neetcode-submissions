class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        res = 0
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(key = lambda x: x[0])
        for i in range(len(cars) - 1, -1, -1):
            time = (target - cars[i][0])/cars[i][1]
            if stack and time <= stack[-1]:
                stack.append(time)
                stack.pop()
            else: 
                stack.append(time)
        return len(stack)
            
 



        return res
