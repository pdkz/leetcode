from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans, last = [], {}
        for i, c in enumerate(s):
            last[c] = i

        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, last[c])
            if i == end:
                ans.append(size)
                size = 0
        return ans
