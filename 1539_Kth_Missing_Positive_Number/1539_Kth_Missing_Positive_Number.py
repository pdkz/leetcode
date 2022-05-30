class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def count_missing_numbers(arr, i):
            return arr[i] - i - 1

        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + (hi-lo) // 2
            if count_missing_numbers(arr, mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo-1]+k-count_missing_numbers(arr, lo-1)