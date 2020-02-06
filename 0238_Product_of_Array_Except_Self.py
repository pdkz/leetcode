class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lhs = [1]
        rhs = [1]
        ans = []
        l = len(nums)
        
        for i in range(l-1):
            lhs.append(nums[i] * lhs[i])
            rhs.insert(0, nums[l-1-i] * rhs[0])
        
        for i in range(l):
            ans.append(lhs[i] * rhs[i])
            
        return ans
