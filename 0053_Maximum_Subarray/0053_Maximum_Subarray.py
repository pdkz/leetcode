class Solution:
    def maxSubArraySlidingWindow(self, nums: List[int]) -> int:
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

    def maxSubArrayDp(self, nums: List[int]) -> int:
        max_subarray_sum = float('-inf')
        subarray_sum = 0
        for n in nums:
            subarray_sum = max(n, n+subarray_sum)
            if max_subarray_sum < subarray_sum:
                max_subarray_sum = subarray_sum
        return max_subarray_sum
