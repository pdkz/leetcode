class Solution:
    def hammingWeight(self, n: int) -> int:
        bitcount = 0
        while n > 0:
            bitcount += 1
            n &= n - 1
        return bitcount