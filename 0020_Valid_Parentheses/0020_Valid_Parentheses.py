class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { ')':'(', '}':'{', ']':'['}

        for c in s:
            if c in pairs.values():
                stack.append(c)
            else:
                if stack and pairs[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False