class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if len(S) == 0:
            return [""]
        
        result = []
        for i in S:
            l = len(result)
            if l == 0:
                result.append(i)
                if i.isdigit() == False:
                    if i.islower():
                        result.append(i.upper())
                    else:
                        result.append(i.lower())
            else:
                for j in range(l):
                    if i.isdigit() == False:
                        if i.islower():
                            result.append(result[j] + i.upper())
                        else:
                            result.append(result[j] + i.lower())
                    result[j] += i
        return result
