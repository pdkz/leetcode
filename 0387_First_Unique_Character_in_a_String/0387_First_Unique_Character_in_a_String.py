class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = collections.Counter(s)
   
        for i, w in enumerate(s):
            if counts[w] == 1:
                return i
        return -1
