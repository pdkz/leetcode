class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 0 or num < 0: 
            return False
        
        m = 0
        while num > 1:
            m = num % 4
            if m > 0 and m < 4:
                return False
            num //= 4

        if m > 0:
            return False
        return True
