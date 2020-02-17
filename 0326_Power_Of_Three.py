class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0 or n < 0: 
            return False
        
        x = n
        y = 0
        while x > 1:
            y = x % 3
            if y > 0 and y < 3:
                return False
            x //= 3

        if y > 0:
            return False
        return True
