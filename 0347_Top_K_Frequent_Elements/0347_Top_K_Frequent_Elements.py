class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return None
        
        ht = collections.Counter(nums)
        sorted_ht = sorted(ht.items(), key=lambda x:-x[1])

        result = []
        for i, item in enumerate(sorted_ht):
            if i > k-1:
                break
            key, val = item
            result.append(key)
        
        return result
