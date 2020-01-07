class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        stack = []
        pairs = {'(':')', '{':'}', '[':']'}
        for bracket in s:
            
            stack.append(bracket)
