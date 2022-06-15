class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = sorted(nums)
        for i, j in enumerate(n):
            if i != j:
                return i
        return n[-1] + 1

    def missingNumber_binary_search(self, nums: List[int]) -> int:
        nums.sort()
        ok, ng = -1, len(nums)

        while abs(ok-ng) > 1:
            mid = ok+(ng-ok) // 2
            if nums[mid] <= mid:
                ok = mid
            else:
                ng = mid
        return nums[ok]+1 if ng == len(nums) else nums[ng]-1