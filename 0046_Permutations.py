"""
# not using recursion
seed = [1,2,3]

l = []
for i in seed:
    l.append(i)
    for j in seed:
        if j in l: 
            continue
        l.append(j)
        for k in seed:
            if k in l: continue
            l.append(k)
            print(i,j,k)
            l.pop()
        l.pop()
    l.pop()

# using recursion   
result = []
perm = []
def make_permutation(seed, n):
    if n == len(seed):
        result.append(perm.copy())
        return perm
    for i in seed:
        if i in perm: continue
        perm.append(i)
        make_permutation(seed, n+1)
        perm.pop()
"""

class Solution:
    def __init__(self):
        self.result = []
        self.perm = []
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.make_permutation(nums, 0)
        return self.result
    
    def make_permutation(self, seed, n):
        if n == len(seed):
            #print(self.perm)
            self.result.append(self.perm.copy())
            return
        for i in seed:
            if i in self.perm: continue
            self.perm.append(i)
            self.make_permutation(seed, n+1)
            self.perm.pop()
