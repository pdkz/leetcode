from typing import List
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N, memo = len(nums), defaultdict()
        def backtrack(i, s):
            nonlocal memo
            if i == N:
                if s == target:
                    memo[(i, s)] = 1
                else:
                    memo[(i, s)] = 0
            if (i,s) not in memo:
                memo[(i,s)] = backtrack(i+1, s+nums[i]) + backtrack(i+1, s-nums[i])
            return memo[(i,s)]
        backtrack(0,0)
        return memo[(0,0)]