from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_bit(n):
            count = 0
            while n > 0:
                count += (n & 1)
                n >>= 1
            return count
        ans = [0] * (n+1)
        for i in range(1,n+1):
            ans[i] = count_bit(i)
        return ans