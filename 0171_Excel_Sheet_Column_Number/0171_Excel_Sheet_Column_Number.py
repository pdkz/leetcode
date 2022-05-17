class Solution:
    def titleToNumber(self, s: str) -> int:
        l = len(s)
        x = 0
        for i, j in enumerate(s):
            n = l - i - 1
            if n > 0:
                x += 26 ** n * (ord(j) - ord('A') + 1)
            else:
                x += ord(j) - ord('A') + 1
        return x
