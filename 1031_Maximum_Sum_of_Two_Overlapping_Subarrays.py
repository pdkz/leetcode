class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix_sum = [0]
        for i, n in enumerate(nums):
            prefix_sum.append(prefix_sum[i] + n)

        max_subarray_sum = float('-inf')
        N = len(nums)
        for i in range(0, N-firstLen+1):
            first_subarray_sum = prefix_sum[i+firstLen] - prefix_sum[i]
            j = 0
            while j < N - secondLen + 1:
                if j+secondLen-1 < i or j > i+firstLen-1:
                    second_subarray_sum = prefix_sum[j+secondLen] - prefix_sum[j]
                    max_subarray_sum = max(max_subarray_sum, first_subarray_sum + second_subarray_sum)
                j += 1
        return max_subarray_sum