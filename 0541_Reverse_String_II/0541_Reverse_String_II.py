class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ''
        l = len(s)
        step = 2*k
        for i in range(0, l, step):
            w = s[i:i+step]
            if len(w) <= k:
                result += w[::-1]
            else:
                head = w[0:k]
                head = head[::-1]
                tail = w[k:]
                result += head + tail
        return result
