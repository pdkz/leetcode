class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        offset = 0
        string = S
        data = []
        
        for i, src, dst in zip(indexes, sources, targets):
            data.append([i, src, dst])        
        data = sorted(data, key=lambda x:x[0])
        
        for i, src, dst in data:
            srclen = len(src)
            if string[i+offset:i+offset+srclen] == src:
                string = string[0:i+offset] + dst + string[i+offset+srclen:]
                offset += len(dst) - srclen

        return string
