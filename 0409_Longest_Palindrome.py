class Solution:
    def longestPalindrome(self, s: str) -> int:
        ht = collections.Counter(s)
        odd = []
        length = 0
        
        for v in ht.values():
            if v % 2 == 0:
                length += v
            elif v % 2 == 1:
                odd.append(v)
        if len(odd) > 0:
            max_odd = max(odd)
            length += max_odd

            idx = odd.index(max_odd)
            del odd[idx]
        
        for v in odd:
            if v > 1:
                length += v - 1
        
        return length
