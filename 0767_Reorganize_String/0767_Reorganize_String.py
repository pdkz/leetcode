import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, S: str) -> str:
        N = len(S)
        
        counter = Counter(S)
        hq = [(-v, k) for k, v in counter.items()]
        
        heapq.heapify(hq)

        A = ""
        for n, c in hq:
            if -n > (N+1) // 2:
                return ""
        
        while len(hq) > 1:
            n1, c1 = heapq.heappop(hq)
            n2, c2 = heapq.heappop(hq)

            A += ''.join([c1, c2])

            if n1 < -1:
                heapq.heappush(hq, (n1+1, c1))
            if n2 < -1:
                heapq.heappush(hq, (n2+1, c2))
        if hq:
            A += hq[0][1]
        return A
