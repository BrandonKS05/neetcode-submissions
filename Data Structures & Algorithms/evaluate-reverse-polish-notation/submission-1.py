class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        operators = {"+", "-", "/", "*"}
        
        def isOperator(s) -> bool:
            return True if s in operators else False

        def operate(s):
            if s == "+":
                b = nums.pop()
                a = nums.pop()
                return a + b
            elif s == "-":
                b = nums.pop()
                a = nums.pop()
                return a - b
            elif s == "*":
                b = nums.pop()
                a = nums.pop()
                return a * b
            elif s == "/":
                b = nums.pop()
                a = nums.pop()
                return int(a/b)
        
        for s in tokens:
            if isOperator(s):
                nums.append(operate(s))
            else:
                nums.append(int(s))
        return nums[0]
                
        
