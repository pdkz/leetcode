class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        curr = 0
        que = deque([(-1, 0)])
        for i, n in enumerate(nums):
            curr += n
            while que and curr <= que[-1][1]:
                que.pop()

            while que and curr - que[0][1] >= k:
                ans = min(ans, i - que.popleft()[0])
            que.append((i, curr))
        return -1 if ans == float('inf') else ans