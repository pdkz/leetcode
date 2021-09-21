class Solution:
    def pivotIndex_00(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1

        l = len(nums)
        s = sum(nums)
        lsum = 0
        rsum = s - nums[0]

        for i in range(0, l):
            if i > 0 and i < l:
                lsum += nums[i-1]
                rsum = s - lsum - nums[i]
            elif i == l - 1:
                rsum = 0

            if lsum == rsum:
                return i

        return -1

    def pivotIndex_01(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0

        prefix_sum = [0]
        for n in nums:
            prefix_sum.append(prefix_sum[-1]+n)

        i = 0
        while i < N:
            left = prefix_sum[i]
            right = prefix_sum[N] - left - nums[i]
            if left == right:
                return i
            i += 1

        return -1
