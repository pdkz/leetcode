class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = sorted(nums)
        for i, j in enumerate(n):
            if i != j:
                return i
        return n[-1] + 1
