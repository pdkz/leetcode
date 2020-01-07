class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        duplicated_indices = []
        prev = nums[0]
        current = 0
        for i, n in enumerate(nums):
            if i == 0: continue
            if prev == n:
                duplicated_indices.append(i)
            prev = n
        
        for i, j in enumerate(duplicated_indices):
            del nums[j-i]
            
        return len(nums)
        
