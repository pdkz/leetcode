class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M, N = len(matrix), len(matrix[0])

        def dfs_l(x,y, matrix):
            if x < 0: return
            matrix[y][x] = 0
            dfs_l(x-1, y,matrix)
        def dfs_r(x,y,matrix):
            if x > N-1: return
            matrix[y][x] = 0
            dfs_r(x+1, y,matrix)
        def dfs_u(x,y,matrix):
            if y < 0: return
            matrix[y][x] = 0
            dfs_u(x, y-1,matrix)
        def dfs_d(x,y,matrix):
            if y > M-1: return
            matrix[y][x] = 0
            dfs_d(x, y+1,matrix)

        candidates = []
        for y in range(M):
            for x in range(N):
                if matrix[y][x] == 0:
                    candidates.append((y,x))

        for y, x in candidates:
            dfs_l(x-1,y,matrix)
            dfs_r(x+1,y,matrix)
            dfs_u(x,y-1,matrix)
            dfs_d(x,y+1,matrix)
