import re

class Solution:
    def romanToInt(self, s: str) -> int:
        num  = 0
        l = len(s)
        skip = False        
        for i, el in enumerate(s):
            if skip == True:
                skip = False
                continue
            if el == 'M':
                num += 1000 
            elif el == 'D':
                num += 500
            elif el == 'C':
                if i < l - 1 and s[i+1] == 'D':
                    num += 400
                    skip = True
                elif i < l - 1 and s[i+1] == 'M':
                    num += 900
                    skip = True
                else:
                    num += 100
            elif el == 'L':
                num += 50
            elif el == 'X':
                if i < l - 1 and s[i+1] == 'L':
                    num += 40
                    skip = True
                    continue
                elif i < l - 1 and s[i+1] == 'C':
                    num += 90
                    skip = True
                else:
                    num += 10
            elif el == 'V':
                num += 5
            elif el == 'I':
                if i < l - 1 and s[i+1] == 'V':
                    num += 4
                    skip = True
                elif i < l - 1 and s[i+1] == 'X':
                    num += 9
                    skip = True
                else:
                    num += 1
        return num
