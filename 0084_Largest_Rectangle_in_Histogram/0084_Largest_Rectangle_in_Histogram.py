def largestRectangleArea(self, heights: List[int]) -> int:
    stack = []
    ans, N = 0, len(heights)
    for i in range(N):
        pos = i
        while stack and stack[-1][1] > heights[i]:
            pos, height = stack.pop()
            ans = max(ans, (i-pos) * height)
        stack.append((pos, heights[i]))
    while stack:
        pos, height = stack.pop()
        ans = max(ans, (N-pos) * height)
    return ans