"""
# not-recursive
def make_subset(n, nums):
    for a, i in enumerate(nums):
        print('[{}][{}]{}'.format(n, a, i))
        for b, j in enumerate(nums):
            if b <= a:
                continue
            print('[{}][{}]{} {}'.format(n+1, a, i , j))
            for c, k in enumerate(nums):
                if c <= b:
                    continue
                print('[{}][{}]{} {} {}'.format(n+2, a, i, j, k))
"""
class Solution:
    def __init__(self):
        self.result = []
        self.subset = []
        self.length = 0
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.length = len(nums)
        
        self.make_subsets(0, 0, sorted(nums))
        self.result.append([])
        
        return self.result
        
    def make_subsets(self, n, p, nums):
        if len(self.result) == self.length:
            return
        
        for a, i in enumerate(nums):
            if n > 0 and a <= p:
                continue
            self.subset.append(i)
            
            if self.subset not in self.result:
                self.result.append(self.subset.copy())
   
            self.make_subsets(n+1, a, nums)
            self.subset.pop()
