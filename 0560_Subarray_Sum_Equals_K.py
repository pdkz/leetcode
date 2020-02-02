class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = len(nums)
        ht = collections.defaultdict(int)
        counter = 0
        sum_subarray = 0
        
        for i in range(l):
            sum_subarray += nums[i]
            for v in ht.values():
                if sum_subarray - v == k:
                    counter += 1
            if sum_subarray == k:
                counter += 1
            
            ht[i] = sum_subarray
        return counter
