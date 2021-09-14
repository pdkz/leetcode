class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        elif N == 2:
            return max(nums)

        dp = [0] * (N+1)

        dp[1] = nums[0]
        dp[2] = nums[1]

        total_first = dp[1]
        total_second = dp[2]

        i = 3
        for n in nums[2:]:
            if i % 2:
                total_first += n
                dp[i] = max(dp[i-1], dp[i-2]+n, dp[i-3]+n, total_first)
            else:
                total_second += n
                dp[i] = max(dp[i-1], dp[i-2]+n, dp[i-3]+n, total_second)
            i += 1
        return dp[N]