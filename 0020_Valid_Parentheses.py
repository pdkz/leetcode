class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        stack = []
        pairs = {'(':')', '{':'}', '[':']'}
        
        if s[0] not in pairs.keys():
            return False
        
        for bracket in s:
            if bracket in pairs.keys():
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                l_bracket = stack.pop()
                r_bracket = pairs[l_bracket]
                
                if r_bracket != bracket:
                    return False        

        if len(stack) > 0:
            return False
        
        return True