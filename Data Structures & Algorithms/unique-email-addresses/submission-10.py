class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            l, l1, l2 = 0, 0, 0
            at = len(email) - 1
            
            serialized = ""

            while l1 < at: 
                if email[l1] == "@":
                    at = l1
                l1 += 1
            plus = at

            while l2 < at:
                if email[l2] == "+":
                    plus = l2
                    break
                l2 += 1

            while l < plus:
                if email[l] != ".":
                    serialized += email[l]
                l += 1
            
            serialized += email[at:]
            
            if serialized not in seen:
                seen.add(serialized)
        return len(seen)
