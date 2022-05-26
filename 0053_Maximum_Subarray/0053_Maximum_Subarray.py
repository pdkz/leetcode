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
        subarray_sum, max_subarray = 0, float('-inf')
        for n in nums:
            subarray_sum += n
            subarray_sum = max(subarray_sum, n)
            max_subarray = max(max_subarray, subarray_sum)
        return max_subarray
