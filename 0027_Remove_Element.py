class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        
        indices = []
        for i, n in enumerate(nums):
            if n == val:
                indices.append(i)
                
        for i, j in enumerate(indices):
            del nums[j-i]
        
        return len(nums)
