class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        mid = 0
        res = n
        while mid < len(flowerbed):
            l = mid - 1
            r = mid + 1
            left_valid = l == -1 or flowerbed[l] == 0 
            right_valid = r == len(flowerbed) or flowerbed[r] == 0
            if flowerbed[mid] == 0 and left_valid and right_valid:
                flowerbed[mid] = 1
                res -= 1
            mid += 1
            print(res)
        return True if res <= 0 else False



