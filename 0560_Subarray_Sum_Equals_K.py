class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ht = defaultdict(int)
        l = len(nums)

        ht[0] = 1
        count = 0
        cumlative_sum = 0
        
        for i in range(0, l):
            cumlative_sum += nums[i]
            
            count += ht.get(cumlative_sum - k, 0)
            ht[cumlative_sum] += 1
            
        return count
