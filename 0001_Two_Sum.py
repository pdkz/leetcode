class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i, n in enumerate(nums):
            j = ht.get(target - n)
            if j != None:
                return [i, j]
            ht[n] = i
