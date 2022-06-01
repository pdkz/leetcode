class Solution:
    def trap(self, height: List[int]) -> int:
        stack, max_h, ans = [], float('-inf'), 0

        for i in range(0, len(height)):
            if max_h <= height[i]:
                while stack:
                    h = stack.pop()
                    ans += max_h-h
            stack.append(height[i])
            max_h = max(max_h, height[i])

        max_h = 0
        while stack:
            h = stack.pop()
            if h < max_h:
                ans += max_h-h
            max_h = max(max_h, h)

        return ans