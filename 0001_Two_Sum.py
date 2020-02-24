class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = collections.defaultdict(int)
        for i, n in enumerate(nums):
            ht[n] = i
            
        for i, n in enumerate(nums):
            diff = target - n
            j = ht.get(diff)
            if j and i != j:
                return [i, j]
        return None
