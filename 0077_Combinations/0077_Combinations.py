class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        used = [False for i in range(n)]

        def backtrack(k, nums, res, tmp, used, begin):
            if len(tmp) >= k:
                res.append(tmp[:])
                return
            for i in range(begin, len(nums)):
                if used[i]:
                    continue
                tmp.append(nums[i])
                used[i] = True
                backtrack(k, nums, res, tmp, used, i+1)
                tmp.pop()
                used[i] = False
        res = []
        backtrack(k, nums, res, [], used, 0)

        return res