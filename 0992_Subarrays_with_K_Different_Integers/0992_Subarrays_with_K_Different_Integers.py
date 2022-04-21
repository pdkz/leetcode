class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(nums: list, k: int):
            window = Counter()
            N = len(nums)
            l, L, ans = 0, 0, 0

            for r in range(N):
                window[nums[r]] += 1

                while len(window) > k:
                    window[nums[l]] -= 1

                    if window[nums[l]] == 0:
                        del window[nums[l]]
                    l += 1

                ans += r-l+1

            return ans
        return helper(nums, k) - helper(nums, k-1)