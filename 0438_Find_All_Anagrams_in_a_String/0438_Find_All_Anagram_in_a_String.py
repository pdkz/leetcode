from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        j, N, M = 0, len(s), len(p)
        ans, counter = [], Counter(p)
        window = Counter()
        for i in range(N):
            window[s[i]] += 1
            while i-j+1 > M:
                window[s[j]] -= 1
                if not window[s[j]]:
                    del window[s[j]]
                j += 1
            if all(window[k] == v for k, v in counter.items()):
                ans.append(j)
        return ans