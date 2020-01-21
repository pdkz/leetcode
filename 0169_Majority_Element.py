class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        k = max(d, key=d.get)
        return k
