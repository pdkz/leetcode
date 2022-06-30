from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, ans = [], [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                j, _ = stack.pop()
                ans[j] = i-j
            stack.append((i,t))
        return ans