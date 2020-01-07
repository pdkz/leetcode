class Solution:
    def lengthOfLastWord(self, s: str) -> int:       
        if len(s) == 0:
            return 0
        
        words = s.split(' ')
        words = [ w for w in words if w != '' ]
        if len(words) == 0:
            return 0
        
        l = len(words[-1])
        return l
