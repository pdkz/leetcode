class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        
        length = len(haystack)
        needle_len = len(needle)
        for i in range(length):
            if i+needle_len > length:
                break
            
            s = haystack[i:i+needle_len]
            if s == needle:
                return i
            
        return -1
