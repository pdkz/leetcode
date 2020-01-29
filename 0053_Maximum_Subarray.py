class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)

        max_subarray = nums[0]
        sum_subarray = max_subarray

        for i in range(1,l):
            if sum_subarray < 0:
                sum_subarray = nums[i]
            else:
                sum_subarray += nums[i]

            if sum_subarray > max_subarray:
                max_subarray = sum_subarray

        return max_subarray
