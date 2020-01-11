class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l = len(nums)
        if l == 0 or l == 1: return False
        
        d = collections.Counter(nums)
        max_v = max(d.values())
        if max_v > 1:
            return True
        return False
