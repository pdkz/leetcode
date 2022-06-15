from collections import deque
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        j, ans, pos, que = 0, 0, 0, deque()
        N, counter = len(nums), 0

        for i in range(N):
            while counter > k:
                if nums[j] % 2:
                    counter -= 1
                    que.popleft()
                    pos = que[0]
                j += 1
            if counter == k:
                ans += pos - j + 1

            if nums[i] % 2:
                que.append(i)
                pos = que[0]
                counter += 1

        while counter > k:
            if nums[j] % 2:
                counter -= 1
                que.popleft()
                pos = que[0]
            j += 1
        if counter == k:
            ans += pos - j + 1

        return ans