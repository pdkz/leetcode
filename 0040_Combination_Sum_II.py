class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        useds = [False for i in range(len(candidates))]
        res = []

        candidates.sort()
        self.backtrack(candidates, res, [], target, useds, 0)

        return res

    def backtrack(self, candidates, res, tmp, target, useds, begin):
        total = sum(tmp)
        if total > target:
            return
        if total == target:
            res.append(tmp[:])
            return
        for i in range(begin, len(candidates)):
            if useds[i]:
                continue
            if i > 0 and not useds[i-1] and candidates[i-1] == candidates[i]:
                continue

            useds[i] = True
            tmp.append(candidates[i])

            self.backtrack(candidates, res, tmp, target, useds, i+1)

            tmp.pop()
            useds[i] = False
