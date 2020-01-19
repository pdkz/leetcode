class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d = collections.Counter(A)
        l = len(A)
        k_N = [k for k, v in d.items() if v == l // 2]
        
        return k_N[0]
