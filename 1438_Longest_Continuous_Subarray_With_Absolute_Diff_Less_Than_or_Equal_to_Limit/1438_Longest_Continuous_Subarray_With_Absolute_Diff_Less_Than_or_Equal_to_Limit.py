from collections import Counter
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        counter = Counter()
        ans = -1
        j = 0
        for i, n in enumerate(nums):
            counter[n] += 1
            while(max(counter.keys()) - min(counter.keys())) > limit:
                counter[nums[j]] -= 1
                if counter[nums[j]] == 0:
                    del counter[nums[j]]
                j += 1
            ans = max(ans, i-j+1)
        return ans