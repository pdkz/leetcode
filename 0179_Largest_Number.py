from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x, y):
            a, b = int(x+y), int(y+x)
            if a < b:
                return 1
            elif a > b:
                return -1
            else:
                return 0

        nums = sorted(map(str, nums), key=cmp_to_key(cmp))
        ans = ''.join(nums).lstrip('0')

        return ans if ans else '0'