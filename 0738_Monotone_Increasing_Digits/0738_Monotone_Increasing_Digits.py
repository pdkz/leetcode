class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10:
            return n

        s = str(n)
        N, begin = len(s), float('inf')
        for i in range(N):
            if i > 0:
                if s[i-1] == s[i]:
                    begin = min(begin, i)
                elif s[i-1] < s[i]:
                    begin = float('inf')
                elif s[i-1] > s[i]:
                    t = N-i if begin == float('inf') else N-begin
                    x = pow(10,t)
                    return n // x * x - 1
        return n