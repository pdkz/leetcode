class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N, sorted_nums = len(nums), sorted(nums)
        if all([nums[i] == sorted_nums[i] for i in range(0, N)]):
            return 0

        l, r = -1, -1
        for i in range(0, N):
            if nums[i] != sorted_nums[i]:
                l = i
                break

        for i in range(N-1, -1, -1):
            if nums[i] != sorted_nums[i]:
                r = i
                break

        return r-l+1