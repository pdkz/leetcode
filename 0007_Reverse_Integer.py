class Solution:
    def reverse(self, x: int) -> int:      
        s = str(x)
        l = len(s)
        output = ''
        zero_flag = False
        
        if s[-1] == '0':
            zero_flag = True
        
        for i in range(l):
            p = s[l - i - 1]
            if p == '0' and zero_flag is True:
                output = '0'
            elif p == '-':
                output = '-' + output  
            else:
                zero_flag = False
                if output == '0':
                    output = ''
                output += p
        
        o = int(output)
        if o > pow(2, 31) - 1 or o < pow(-2, 31):
            return 0
        
        return int(output)
