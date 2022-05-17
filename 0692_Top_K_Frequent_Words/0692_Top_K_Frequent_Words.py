import heapq
from collections import Counter

class Word:
    def __init__(self, word):
        self.word = word
    def __lt__(self, other):
        return self.word < other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_count = Counter(words)
        hq = []

        for w, c in words_count.items():
            obj = Word(w)
            heapq.heappush(hq, (-c, obj))

        res = []
        i = 0
        while i < k:
            res.append(heapq.heappop(hq)[1].word)
            i += 1
        return res