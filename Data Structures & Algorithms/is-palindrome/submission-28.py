class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s) - 1
        clean = s.lower()
        while (left < right):
            if not clean[left].isalnum():
                left += 1
            elif not clean[right].isalnum():
                right -= 1
            else:
                if clean[left] != clean[right]:
                    return False
                left +=1
                right -= 1
            
        return True
                