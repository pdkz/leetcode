class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = collections.defaultdict(list)
        
        for i, n in enumerate(nums):
            h[n].append(i)
            l = len(h[n])
            if l > 1:
                for j in range(l-1):
                    if i - h[n][j] <= k:
                        return True
        return False
