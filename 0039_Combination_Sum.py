class Solution:
    def __init__(self):
        self.tmp = []
        self.result = []
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.find_comb(target, candidates)
        return self.result
        
    def find_comb(self,t, nums):
        if t < 0:
            return 
        for i in nums:
            if i == t:
                self.tmp.append(i)
                ans = sorted(self.tmp)
                if ans not in self.result:
                    self.result.append(ans)
                self.tmp.pop()
            else:
                n = t - i
                self.tmp.append(i)
                self.find_comb(n, nums)
                self.tmp.pop()
