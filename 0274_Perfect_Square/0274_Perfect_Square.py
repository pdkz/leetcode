import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        dp[1] = 1
        max_root = int(math.sqrt(n))
        for a in range(2, n+1):
            for x in range(1, max_root+1):
                perfect_sqrt = x ** 2
                if a > perfect_sqrt:
                    dp[a] = min(dp[a - perfect_sqrt] + 1, dp[a])
                elif a == perfect_sqrt:
                    dp[a] = 1
                else:
                    break
        return dp[-1]