class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        subset = []
        l = len(nums)
        
        subset.append([])
        
        for i in nums:
            subset.append([i])
        
        for n in range(0,l-1):
            for i in subset:
                if len(i) != n+1: 
                    continue
                offset = nums.index(max(i))
                
                for j in nums[offset+1:]:
                    subset.append(i+[j])
        
        return subset
