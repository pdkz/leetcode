class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        N = len(nums)
        maximum_length, length = 1, 1
        for i in range(1, N):
            if nums[i-1] < nums[i]:
                length += 1
            else:
                length = 1
            maximum_length = max(length, maximum_length)
        return maximum_length