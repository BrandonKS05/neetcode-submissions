class Solution:
    calculated = {}
    def climbStairs(self, x: int) -> int:
        if x in self.calculated:
            return self.calculated[x]
        if x == 1:
            return 1

        if x == 2:
            return 2

        self.calculated[x] = self.climbStairs(x - 2) + self.climbStairs(x - 1)
        ######
        answer = self.calculated[x]
        return answer



        
        

        
    
    
    
    



        