class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        useds = [False for i in range(len(nums))]
        nums.sort()

        def backtrack(res, tmp):
            nonlocal useds
            if len(tmp) == len(nums):
                res.append(tmp[:])
                return

            for i, n in enumerate(nums):
                if useds[i]:
                    continue
                if (i > 0 and not useds[i-1] and nums[i] == nums[i-1]):
                    continue
                tmp.append(n)
                useds[i] = True
                backtrack(res, tmp)
                tmp.pop()

                useds[i] = False
        backtrack(res, [])

        return res