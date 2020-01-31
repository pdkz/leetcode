class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ds = collections.Counter(s)
        dt = collections.Counter(t)
        
        if len(ds) > len(dt):
            d1 = ds
            d2 = dt
        else:
            d1 = dt
            d2 = ds
            
        for k in d1.keys():
            if d2[k] == 0:
                return k
            elif d1[k] != d2[k]:
                return k
            
            
