class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M= len(obstacleGrid)
        N = len(obstacleGrid[0])
        paths = [[0] * N for _ in range(M)]

        for i in range(M):
            if i == 0:
                paths[i][0] = 1 if not obstacleGrid[i][0] else 0
            else:
                paths[i][0] = 1 if not obstacleGrid[i][0] and paths[i-1][0] else 0
        for j in range(N):
            if j == 0:
                paths[0][j] = 1 if not obstacleGrid[0][j] else 0
            else:
                paths[0][j] = 1 if not obstacleGrid[0][j] and paths[0][j-1] else 0

        for i in range(1, M):
            for j in range(1, N):
                if not obstacleGrid[i][j]:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]
                else:
                    paths[i][j] = 0
        return paths[M-1][N-1]
                    