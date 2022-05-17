class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        return self.rec(candidates, 0, target, [], res)
        
    def rec(self, nums, s, t, tmp, res):
        if t < 0:
            return 
        if s == t:
            res.append(tmp.copy())
            return

        for n in nums:
            if s + n > t:
                return
            elif len(tmp) > 0 and n < tmp[-1]:
                continue
            s += n
            tmp.append(n)
            self.rec(nums, s, t, tmp, res)
            tmp.pop()
            s -= n
