class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        #brandon
        n = len(word)
        hashmap = {} 
        count = 0
        for key in keyboard:
            hashmap[key] = count
            count += 1
        total = hashmap[word[0]]
        for i in range(1, n):
            prev = word[i - 1]
            diff = abs(hashmap[word[i]] - hashmap[prev])
            total += diff
        return total

        





        