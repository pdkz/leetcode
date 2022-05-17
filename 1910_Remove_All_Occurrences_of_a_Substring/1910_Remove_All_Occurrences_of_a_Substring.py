class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        N = len(part)

        for c in s:
            stack.append(c)
            if stack and len(stack) >= N and ''.join(stack[-N:]) == part:
                for i in range(N):
                    stack.pop()

        return ''.join(stack)