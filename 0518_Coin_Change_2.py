class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = []
        for i in range(N):
            dp.append([0 for _ in range(amount+1)])

        for i in range(N):
            dp[i][0] = 1
            for j in range(amount+1):
                if coins[i] <= j:
                    if i > 0: dp[i][j] = dp[i][j-coins[i]] + dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-coins[i]]
                elif i > 0:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]