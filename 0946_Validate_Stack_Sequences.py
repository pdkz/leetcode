class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        
        while len(popped) > 0:
            if len(pushed) == 0 and popped[0] != stack[-1]:
                return False
            
            if len(stack) > 0 and popped[0] == stack[-1]:
                stack.pop()
                popped.pop(0)
            else:
                stack.append(pushed.pop(0))

        return True
