class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        """
        a = [0 for i in range(26)]
        b = [0 for i in range(26)]
        
        for word in A[0]:
            for ch in word:
                a[ord(ch) - ord('a')] += 1
            
        for word in A[1:]:
            b = [0 for i in range(26)]
            for ch in word:
                b[ord(ch) - ord('a')] += 1
            for i in range(26):
                a[i] = min(a[i], b[i])
        
        result = []
        for i in range(26):
            for j in range(a[i]):
                result.append(chr(ord('a') + i))
        return result
        """
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
                
