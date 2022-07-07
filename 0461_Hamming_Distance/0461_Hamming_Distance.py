class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n, d = x ^ y, 0
        while n > 0:
            d += n & 1
            n >>= 1
        return d