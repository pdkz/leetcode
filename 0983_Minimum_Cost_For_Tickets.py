class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #
        # days = [1,4,6,7,8,20], costs = [2,7,15] # 1-day,7-days.30-days
        #
        # days: 0 1 2.3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
        #.        +.    +.  + + +                                 +
        # days 0 dp[0]
        # days 1 dp[0] + cost[0]
        # days 2 -
        # days 3 -
        # days 4 dp[3] + cost[0]
        # days 5
        # days 6 dp[5] + cost[0]
        # days 7 min(dp[6] + cost[0], dp[6-7+1] + cost[2])
        # days 8 min(dp[7] + cost[0], dp[7-7+1] + cost[2])
        # ---
        N = days[-1]
        s = set(days)
        dp = [0] * (N+1)
        for i in range(1, N+1):
            cost_1  = dp[i-1]
            cost_7  = dp[i-7] if (i-7) > 0 else 0
            cost_30 = dp[i-30] if (i-20) > 0 else 0
            if i in s:
                #dp[i] = min(cost_1 + costs[0], min(cost_7+costs[1], cost_30+costs[2]))
                dp[i] = min(cost_1 + costs[0], cost_7+costs[1], cost_30+costs[2])
            else:
                dp[i] = dp[i-1]
        return dp[N]