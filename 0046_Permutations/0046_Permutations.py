class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        useds = [False for i in range(len(nums))]

        def backtrack(nums, res, tmp):
            if len(tmp) == len(nums):
                res.append(tmp[:])
                return

            for i, n in enumerate(nums):
                if useds[i]:
                    continue

                tmp.append(n)
                useds[i] = True

                backtrack(nums, res, tmp)

                tmp.pop()
                useds[i] = False

        backtrack(nums, res, [])
        return res