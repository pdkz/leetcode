class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 2:
            return nums[0] == target or nums[1] == target

        l = 0
        r = len(nums) - 1

        while (l<r and nums[l]==nums[r]):
            l += 1

        while (l<=r):
            m = (l+r) // 2
            if nums[m] == target:
                return True

            if nums[m] < nums[l]:
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] > target and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
        return False