class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        
        l = len(nums)
        s = sum(nums)
        lsum = 0
        rsum = s - nums[0]
        
        for i in range(0, l):
            if i > 0 and i < l:
                lsum += nums[i-1]
                rsum = s - lsum - nums[i]
            elif i == l - 1:
                rsum = 0
            
            if lsum == rsum:
                return i
                            
        return -1
