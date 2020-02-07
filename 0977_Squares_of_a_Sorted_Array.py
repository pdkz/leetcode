class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        nums = []
        for i in A:
            nums.append(i ** 2)
        nums = sorted(nums)
        return nums
