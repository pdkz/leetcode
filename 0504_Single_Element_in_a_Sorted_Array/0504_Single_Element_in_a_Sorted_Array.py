class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        begin, end = 0, N - 1
        while begin <= end:
            m = (begin+end) // 2
            if m > 0 and nums[m] == nums[m-1]:
            # m > 0 のエッジケースに注意
                if m % 2:
                    begin = m + 1
                else:
                    end = m - 2
            elif m < N-1 and nums[m] == nums[m+1]:
            # m < N-1 のエッジケースに注意
                if m % 2:
                    end = m - 2
                else:
                    begin = m + 1
            else:
                return nums[m]
        return nums[begin]