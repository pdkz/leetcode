class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ax = 0
        bx = 0
        n = len(a) - 1
        for i, d in enumerate(a):
            if d == '0': continue
            ax += 2 ** (n - i)
        
        n = len(b) - 1
        for i, d in enumerate(b):
            if d == '0': continue
            bx += 2 ** (n - i)
            
        cx = ax + bx
        binstr = ''
        x = cx
        while(1):
            m = x % 2
            if m == 0:
                binstr = '0' + binstr
            else:
                binstr = '1' + binstr
            x = x // 2
            if x == 0: break
        
        return binstr
