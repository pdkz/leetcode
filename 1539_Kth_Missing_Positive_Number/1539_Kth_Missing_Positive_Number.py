class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_count = 0
        prev_idx = prev_n = 0
        ans = 0

        for i, n in enumerate(arr):
            missing_count = n - i - 1
            if prev_idx <= k and k <= missing_count:
                idx = self.binary_search(prev_idx+1, missing_count, k)
                ans = prev_n + idx + 1
                break

            prev_idx = missing_count
            prev_n = n

        if ans == 0:
            ans = arr[-1] + k - missing_count
        return ans

    def binary_search(self, i, j, k):
        arr = [_ for _ in range(i, j+1)]
        begin = 0
        end = len(arr)-1
        while begin <= end:
            m = (begin+end) // 2
            if arr[m] < k:
                begin = m + 1
            elif arr[m] > k:
                end = m - 1
            else:
                break
        return m