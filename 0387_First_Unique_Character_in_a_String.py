class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0: return -1
        if len(s) == 1: return 0
        from collections import Counter
        from collections import defaultdict
        
        wordcount = Counter()
        wordindex = defaultdict(int)
        
        for i, w in enumerate(s):
            wordcount[w] += 1
            if w not in wordindex: wordindex[w] = i
        
        words = [k for k,v in wordcount.items() if v == 1]
        if len(words) == 0:
            return -1
        
        counts = {k:v for k, v in wordindex.items() if k in words}
        idx = min(counts.values())
        
        return idx
