class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        if nums[lo] <= nums[hi]:
            return nums[lo]

        while (lo < hi):
            mid = lo + (hi-lo) // 2
            if mid > 0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[lo] <= nums[mid] and nums[hi] < nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return nums[lo]
