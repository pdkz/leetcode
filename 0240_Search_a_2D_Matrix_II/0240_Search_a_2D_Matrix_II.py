class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N = len(matrix[0])
        for nums in matrix:
            lo, hi = 0, N-1
            while lo <= hi:
                mid = lo + (hi-lo) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False