class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tail = digits[-1]
        pos  = -1
        
        elements = []
        if tail == 9:
            for i, d in enumerate(digits[::-1]):                
                if d != 9:
                    pos = len(digits) - 1 - i                    
                    break
                elements.append(0)
                digits[pos-1] += 1
        else:
            tail += 1
            elements = [tail]
            
        l = digits[:pos] 
        l += elements
        return l
