class Solution:
    def mySqrt(self, x: int) -> int:
        ok, ng = -1, x+1

        while abs(ok-ng) > 1:
            mid = ok + (ng-ok) // 2
            if mid * mid <= x:
                ok = mid
            else:
                ng = mid
        return ok