class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        def helper1(nums):
            dp = [0] * (len(nums) - 1)
            dp[0] = nums[0]
            dp[1] = max(dp[0], nums[1])
            for i in range(2, len(nums)-1) :
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            return dp[-1]

        def helper2(nums):
            dp = [0] * (len(nums))
            dp[1] = nums[1]
            dp[2] = max(dp[1], nums[2])
            for i in range(2, len(nums)) :
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            return dp[-1]

        return max(helper1(nums), helper2(nums))