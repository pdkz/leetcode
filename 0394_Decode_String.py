class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        l = len(s)
        d = ''
        brackets = 0

        decoded_string = ''
        stack = Stack()

        while i < l:
            c = s[i]
            if c == '[':
                brackets += 1
                stack.push(d)
                d = ''
            elif c == ']':
                brackets -= 1
                c_ = stack.pop()
                n_ = stack.pop()

                decoded = int(n_) * c_
                if brackets > 0:
                    stack.push(decoded)
                else:
                    decoded_string += decoded
            elif c.isdigit():
                d += c
            else:
                if brackets > 0:
                    stack.push(c)
                else:
                    decoded_string += c

            i += 1
            
        return decoded_string
    

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, c):
        if c.isdigit():
            self.stack.append(c)
        else:
            if len(self.stack) > 0:
                if self.stack[-1].isdigit():
                    self.stack.append(c)
                else:
                    c_ = self.stack.pop()
                    c_ += c
                    self.stack.append(c_)

    def pop(self):
        return self.stack.pop()