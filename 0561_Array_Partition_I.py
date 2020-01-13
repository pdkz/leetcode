class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        total = 0
        for i in range(0, n, 2):
            total += min(sorted_nums[i:i+2])
        return total
