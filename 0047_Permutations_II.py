class Solution:
    def __init__(self):
        self.result = []
        self.perm = []
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.permutate(0, [], nums)
        return self.result
    
    def permutate(self, n, p, nums):
        if n >= len(nums):
            if self.perm not in self.result:
                self.result.append(self.perm.copy())
            return
        
        for a, i in enumerate(nums):
            if n > 0 and a in p:
                continue
            p.append(a)
            self.perm.append(i)
            self.permutate(n+1, p, nums)
            self.perm.pop()
            p.pop()
