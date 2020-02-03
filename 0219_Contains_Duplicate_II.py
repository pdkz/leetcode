class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = collections.defaultdict(int)
        
        for i, n in enumerate(nums):
            if h.get(n) is not None:
                if i - h[n] <= k:
                    return True

            h[n] = i
            
        return False
