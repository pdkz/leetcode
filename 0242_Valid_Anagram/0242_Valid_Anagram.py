class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = collections.Counter([w for w in s])
        dt = collections.Counter([w for w in t])
        
        for k, v in ds.items():
            v_t = dt.get(k)
            if v_t == None:
                return False
            if v_t != v:
                return False
            
        for k, v in dt.items():
            v_s = ds.get(k)
            if v_s == None:
                return False
            if v_s != v:
                return False
            
        return True
