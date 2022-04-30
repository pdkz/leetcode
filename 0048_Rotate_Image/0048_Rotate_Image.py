class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def reverse(matrix, N):
            N = len(matrix)
            for i in range(N):
                lo, hi = 0, N-1
                while lo < hi:
                    matrix[i][lo], matrix[i][hi] = matrix[i][hi], matrix[i][lo]
                    lo += 1
                    hi -= 1
            return matrix

        N = len(matrix)
        matrix = reverse(matrix, N)

        for i in range(0, N-1):
            for j in range(0, N-i-1):
                matrix[i][j], matrix[N-1-j][N-1-i] = matrix[N-1-j][N-1-i], matrix[i][j]
        return matrix