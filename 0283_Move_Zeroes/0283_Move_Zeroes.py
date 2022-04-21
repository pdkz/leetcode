class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l == 0:
            return []
        
        i = 0
        while i < l:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                l -= 1
            else:
                i += 1
        return nums
