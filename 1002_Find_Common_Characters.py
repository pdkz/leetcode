class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        words = [collections.Counter(w) for w in A]
        l = len(words)
        result = []
        for ch, v in words[0].items():
            count = []
            for word in words[1:]:
                c = word.get(ch)
                if c != None and c > 0:
                    count.append(word[ch])
            if len(count) == l - 1:
                count.append(v)

                num = min(count)
                for i in range(num):
                    result.append(ch)
        
        return result
                
