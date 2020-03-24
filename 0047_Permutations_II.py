class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 0:
            return res

        nums.sort()
        visited = [False for i in range(len(nums))]
        
        self.permute(nums, [], res, visited)
        
        return res
    
    def permute(self, nums, l, res, visited):
        nlen = len(nums)
        if len(l) == nlen:
            res.append(l.copy())
            return

        i = 0
        while i < nlen:
            if visited[i]:
                i += 1
                continue
            
            visited[i] = True
            l.append(nums[i])
            self.permute(nums, l, res, visited)
            l.pop()
            visited[i] = False
            
            while i+1 < nlen and nums[i] == nums[i+1]:
                i += 1
            i += 1
