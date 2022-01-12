class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        ht = {c:i for i,c in enumerate(s)}
        for i, c in enumerate(s):
            if c in stack:
                continue
            while stack and stack[-1] > c and i < ht[stack[-1]]:
                stack.pop()
            stack.append(c)

        return ''.join(stack)