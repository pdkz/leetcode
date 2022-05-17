class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [0] * (N+2)
        dp[0] = 0
        dp[1] = cost[0]

        for i in range(2, N+2):
            if i < N+1:
                dp[i] = min(dp[i-2]+cost[i-1], dp[i-1]+cost[i-1])
            else:
                dp[i] = min(dp[i-2], dp[i-1])
        return dp[N+1]