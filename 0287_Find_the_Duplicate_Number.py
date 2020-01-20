class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        keys = [k for k, v in d.items() if v > 1]
        return keys[0]
