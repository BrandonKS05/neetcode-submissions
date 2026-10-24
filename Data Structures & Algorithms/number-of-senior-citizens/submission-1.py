class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        freq = []
        for passenger in details:
            first = passenger[11]
            second = passenger[12]
            tmp = [first, second]
            age = "".join(tmp)
            age = int(age)
            if age > 60:
                count += 1
        return count
            
