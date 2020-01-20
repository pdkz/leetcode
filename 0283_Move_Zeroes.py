class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        c = 0
        l = len(nums)
        
        while(c < l):
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
            else:
                i += 1
            c += 1
