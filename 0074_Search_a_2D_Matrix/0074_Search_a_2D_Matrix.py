class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        lo, hi = 0, M*N-1

        while lo <= hi:
            mid = lo + (hi-lo) // 2

            i, j = mid // N, mid % N
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False