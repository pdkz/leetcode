class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)
        if ns == 0:
            return True
        if nt == 0:
            return False

        i = 0
        for j in range(nt):
            if s[i] == t[j]:
                i += 1
            if i > ns-1:
                return True
        return False