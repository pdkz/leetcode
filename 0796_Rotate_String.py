class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True

        # bruteforce
        sz = len(A)
        
        for i in range(sz):
            rotated = A[sz-i-1:] + A[0:sz-i-1]
            if rotated == B:
                return True
        return False
