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
    def permute(self, nums: List[int]) -> List[List[int]]:
        r = []
        self.make_permutation(nums, [], r)
        return self.result
        
    def make_permutation(self, nums, l, r):
        if len(l) == len(nums):
            r.append(l.copy())
            return

        for n in nums:
            if n not in l:
                l.append(n)
                self.make_permutation(nums, l, r)
                if len(l) > 0:
                    l.pop()
