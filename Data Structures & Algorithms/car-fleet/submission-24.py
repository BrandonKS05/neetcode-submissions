class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = {}
        for i in range(len(position)):
            cars[position[i]] = speed[i]
        print(cars)
        position.sort()
       
        for i in range(len(position)-1 , -1, -1):
            time = (target - position[i])/cars[position[i]]
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
        


        return len(stack)

