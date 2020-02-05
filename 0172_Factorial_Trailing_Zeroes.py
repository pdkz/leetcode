class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        
        a = 0
        x = 1
        y = 0
        while(True):
            y = n // (5 ** x)
            a += y
            x += 1
            
            if y == 0:
                break
            
        return a
