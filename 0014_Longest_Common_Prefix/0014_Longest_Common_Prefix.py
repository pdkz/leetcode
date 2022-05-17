class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self.common_prefix(strs)

    def common_prefix(self, strs: List[str]) -> str:
        min_str = len(min(strs, key=len))
        N = len(strs)
        lo = 0
        hi = min_str - 1
        prefix = ''

        while (lo<=hi):
            mid = lo + (hi-lo) // 2
            if self.is_common_prefix(strs, N, lo, mid):
                prefix = strs[0][0:mid+1]
                lo = mid + 1
            else:
                hi = mid - 1
        return prefix

    def is_common_prefix(self, strs, n, begin, end):
        t = strs[0]
        for i in range(n):
            s = strs[i]
            for j in range(begin, end+1):
                if s[j] != t[j]:
                    return False
        return True

    def solve(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        common_prefix = []
        trial = min([len(el) for el in strs])

        for i in range(trial):
            if i+1 > trial:
                break

            prefix = [s[:i+1] for s in strs]
            if len(set(prefix)) != 1:
                break
            common_prefix = prefix.copy()

        if len(common_prefix) == 0: return ""

        return common_prefix[0]
