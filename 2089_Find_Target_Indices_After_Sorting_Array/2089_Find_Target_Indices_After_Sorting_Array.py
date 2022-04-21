class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, k):
            l = 0
            r = len(nums)

            while l < r:
                m = (l+r) // 2
                if nums[m] < k:
                    l = m + 1
                else:
                    r = m
            return l

        nums.sort()

        begin = binary_search(nums, target)
        end = binary_search(nums, target + 1)

        return [i for i in range(begin, end)] if begin < end else []