class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ht = defaultdict(int)
        prefix_sum = 0
        max_subarray_length = float('-inf')

        i = 0
        ht[0] = 0
        for n in nums:
            prefix_sum += nums[i]
            ht[prefix_sum] = min(ht.get(prefix_sum, float('inf')), i+1)

            j = ht.get((prefix_sum - k), None)
            if j != None and j >= 0:
                max_subarray_length = max(i-j+1, max_subarray_length)
            i += 1
        return max_subarray_length if max_subarray_length != float('-inf') else 0