from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans, N = [], 0
        def dfs(i, begin, nums):
            nonlocal ans
            if sum(nums) > n:
                return
            if i == k:
                if sum(nums) == n:
                    ans.append(nums.copy())
                return

            for j in range(begin, N):
                if i > 0 and j <= nums[i-1]:
                    continue

                nums.append(j)
                dfs(i+1, begin+1,nums)
                nums.pop()

        dfs(0,1,[])
        return ans