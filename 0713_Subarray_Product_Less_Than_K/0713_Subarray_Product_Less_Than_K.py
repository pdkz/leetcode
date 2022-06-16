class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        j, ans, product = 0, 0, 1
        for i in range(N):
            product *= nums[i]
            while j < i and product >= k:
                product //= nums[j]
                j += 1
            if product < k:
                ans += i-j+1
        return ans