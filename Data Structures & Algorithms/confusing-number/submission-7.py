class Solution:
    def confusingNumber(self, n: int) -> bool:
        confusing_num = ["0","1","6","8","9"]
        p = ["0", "1", "8"]
        newstring = str(n)
        if newstring in p:
            return False
        if len(set(newstring)) == 1 and newstring[0] in p:
            return False
        for string in newstring:
            if string not in confusing_num:
                return False
        return True

