class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Time complexity: O(N)
        """
        count = { n for n in nums if n > 0 }
        if not count:
            return 1
        max_n = max(count)

        for i in range(1, max_n+1):
            if i not in count:
                return i
        return i+1

    def firstMissingPositive_01(self, nums: List[int]) -> int:
        """
        Time complexity: O(NlogN)
        """
        nums.sort()

        i, missing_positive = 0, 1
        while i < len(nums) and nums[i] < 1:
            i += 1

        for j in range(i, len(nums)):
            if nums[j] == missing_positive:
                missing_positive += 1
            elif nums[j] > missing_positive:
                return missing_positive
        return missing_positive