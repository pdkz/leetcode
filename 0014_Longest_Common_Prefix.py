class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        common_prefix = []
        trial = min([len(el) for el in strs])
        
        for i in range(trial):
            if i+1 > trial:
                break
            
            prefix = [s[:i+1] for s in strs]
            if len(set(prefix)) != 1:
                break
            common_prefix = prefix.copy()
        
        if len(common_prefix) == 0: return ""
        
        return common_prefix[0]
