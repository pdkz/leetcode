class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]

    def rob_(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 3:
            return max(nums)

        dp = [0] * (N+1)

        dp[1] = nums[0]
        dp[2] = nums[1]

        total_first = dp[2]
        total_second = dp[1]

        i = 3
        for n in nums[2:]:
            if i % 2 == 0:
                total_first += n
                dp[i] = max(dp[i-1], dp[i-2]+n, dp[i-3]+n, total_first)
            else:
                total_second += n
                dp[i] = max(dp[i-1], dp[i-2]+n, dp[i-3]+n, total_second)
            i += 1
        return dp[N]