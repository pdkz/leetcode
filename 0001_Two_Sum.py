class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx, i in enumerate(nums):
            j = target - i
            if j < 0:
                continue
            if j in nums and nums.index(j) > idx:
                a = nums.index(i)
                b = nums.index(j)
                return [a, b]
