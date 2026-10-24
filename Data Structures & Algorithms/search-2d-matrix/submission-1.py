class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = rows - 1
        while l <= r:
            mid = (l + r)// 2
            if matrix[mid][0] <= target <= matrix[mid][cols-1]:
                break
            elif matrix[mid][0] > target: 
                r = mid - 1
            elif matrix[mid][cols - 1] < target:
                l = mid + 1

        pivot = mid
        l = 0
        r = cols - 1
        while l <= r:
            mid = (l + r)// 2
            if matrix[pivot][mid] == target:
                return True
            elif matrix[pivot][mid] > target:
                r = mid - 1
            elif matrix[pivot][mid] < target:
                l = mid + 1
        return False
        