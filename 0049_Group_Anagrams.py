class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = collections.defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            ht[sorted_s].append(s)
        return ht.values() 
