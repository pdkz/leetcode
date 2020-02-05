class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ht = collections.Counter(nums)
        sorted_items = sorted(ht.items(), key=lambda x:-x[0])
        
        n = 0
        p = 0
        for i, item in enumerate(sorted_items):
            key, val = item
            n += val
            
            if n == k or (p < k and k <= n):
                return key 
            p = n
