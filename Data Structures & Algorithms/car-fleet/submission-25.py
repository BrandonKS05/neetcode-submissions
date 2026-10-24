class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
    
        cars = list(zip(position, speed))
        cars.sort(key = lambda x : x[0])
       
        for i in range(len(cars)-1 , -1, -1):
            pos, speed = cars[i]
            time = (target - pos)/speed
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
        


        return len(stack)

