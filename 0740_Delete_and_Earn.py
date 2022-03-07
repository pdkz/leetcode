class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        counter = Counter(nums)

        max_value = max(counter)
        min_value = min(counter)

        dp = [0] * (max_value+1)

        dp[0] = 0
        dp[min_value] = min_value * counter[min_value]
        nums = sorted(list(counter.keys()))

        for i in range(2, max_value+1):
            dp[i] = max(dp[i-1], i * counter[i] + dp[i-2])
        return dp[-1]