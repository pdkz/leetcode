class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ht = collections.Counter(nums)
        
        keys = sorted(ht.keys(), reverse=True)
        if len(keys) < 3:
            return keys[0]
        
        return keys[2]
