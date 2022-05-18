class Solution:
    def decodeString(self, s: str) -> str:
        i, L = 0, len(s)
        stack = []
        while (i < L):
            if s[i] != ']':
                stack.append(s[i])
            else:
                tmp = ''
                while stack and stack[-1] != '[':
                    c = stack.pop()
                    tmp = c + tmp
                stack.pop()
                
                num = ''
                while stack and stack[-1].isnumeric():
                    n = stack.pop()
                    num = n + num

                stack.append(tmp * int(num))
            i += 1
        return ''.join(stack)