class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_subarray_length = float('inf')
        subarray_sum = 0
        l = 0
        r = 0
        N = len(nums)
        for r in range(N):
            subarray_sum += nums[r]
            while target <= subarray_sum:
                min_subarray_length = min(min_subarray_length, r-l+1)
                subarray_sum -= nums[l]
                l += 1
        return min_subarray_length if not min_subarray_length == float('inf') else 0