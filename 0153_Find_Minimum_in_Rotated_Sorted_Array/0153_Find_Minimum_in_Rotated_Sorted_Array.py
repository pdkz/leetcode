class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        low = 0
        high = len(nums) - 1

        while(low <= high):
            mid = (low + high) // 2

            if nums[low] > nums[mid]:
                if high - low == 1:
                    return nums[low]
                high = mid
            elif nums[high] < nums[mid]:
                if high - low == 1:
                    return nums[high]
                low = mid
            else:
                return nums[low]
