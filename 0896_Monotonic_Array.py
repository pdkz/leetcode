class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        u = 0
        d = 0
        p = 0
        for i, j in enumerate(A):
            if i > 0:
                if p < j:
                    u += 1
                elif p > j:
                    d += 1
            if u > 0 and d > 0:
                return False
            p = j
        return True

