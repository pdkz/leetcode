from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        M = len(s1)
        N = len(s2)

        ht1 = Counter(s1)
        ht2 = Counter(s2[:M])

        for i in range(N-M+1):
            window = s2[i:i+M]

            if all([ht1[s] == ht2[s] for s in s1]):
                return True

            ht2[s2[i]] -= 1
            if i+M < N:
                ht2[s2[i+M]] += 1
        return False