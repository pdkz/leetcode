class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        begin = 0
        end = begin + 1
        
        n = len(nums)
        max_subarray = sum(nums[begin:end])
        
        while(begin < n and end < n+1):
            subarray = nums[begin:end]
            sum_subarray = sum(subarray)

            if sum_subarray > max_subarray:
                max_subarray = sum_subarray

            if sum_subarray < 0:
                begin += 1
                end = begin + 1
            else:
                end += 1
                
        return max_subarray
