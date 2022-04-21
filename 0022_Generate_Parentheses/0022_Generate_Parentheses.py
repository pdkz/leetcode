class Solution:
    def __init__(self):
        self.result = []
        
    def generateParenthesis(self, n: int) -> List[str]:
        self.gen([], n)
        return self.result
        
    def gen(self, brackets,n):
        if len(brackets) == 2*n:
            s = ''.join(brackets)
            r = self.isValid(brackets)
            if r:
                self.result.append(s)
            return

        brackets.append('(')
        self.gen(brackets, n)
        brackets.pop()
        brackets.append(')')
        self.gen(brackets, n)
        brackets.pop()
        
    def isValid(self, brackets):
        n = 0
        for b in brackets:
            if b == '(':
                n += 1
            else:
                n -= 1
            if n < 0:
                return False
        if n == 0:
            return True
        else:
            return False
