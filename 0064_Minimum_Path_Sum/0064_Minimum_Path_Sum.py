from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = []
        for i in range(M):
            dp.append([])
            for j in range(N):
                dp[i].append(float('-inf'))

        dp[0][0] = grid[0][0]
        for r in range(0, M):
            for c in range(0, N):
                if r == 0 and c == 0:
                    continue
                if r > 0 and c > 0:
                    dp[r][c] = min(dp[r-1][c]+grid[r][c], dp[r][c-1]+grid[r][c])
                elif r == 0 and c > 0:
                    dp[r][c] = dp[r][c-1] + grid[r][c]
                elif c == 0 and r > 0:
                    dp[r][c] = dp[r-1][c] + grid[r][c]
        return dp[M-1][N-1]
