class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, res, tmp, start):
            res.append(tmp[:])

            for i in range(start, len(nums)):
                tmp.append(nums[i])
                dfs(nums, res, tmp, i+1)
                tmp.pop()

        res = []
        dfs(nums, res, [], 0)

        return res