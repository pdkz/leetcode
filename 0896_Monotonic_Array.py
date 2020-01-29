class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        up = 0
        down = 0
        prev = 0
        for i, j in enumerate(A):
            if i > 0:
                if prev < j:
                    up += 1
                elif prev > j:
                    down += 1
            if up > 0 and down > 0:
                return False
            prev = j
        return True

