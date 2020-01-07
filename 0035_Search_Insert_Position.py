class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            pos = nums.index(target)
            return pos

        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]
            #print(nums[low], nums[high], nums[mid], guess)
            if guess > target:
                high = mid - 1
            else:
                low = mid + 1
        
        idx = nums.index(guess)
        if guess >= target:
            pos = idx
        else:
            pos = idx + 1
        
        return pos
