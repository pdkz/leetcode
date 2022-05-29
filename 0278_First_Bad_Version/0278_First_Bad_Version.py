class Solution:
    def firstBadVersion(self, n: int) -> int:
        ok, ng = n+1, 0

        while abs(ok-ng) > 1:
            mid = ok + (ng-ok) // 2
            if isBadVersion(mid):
                ok = mid
            else:
                ng = mid

        return ok