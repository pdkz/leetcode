from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set, dist = set(wordList), 1
        que = deque([(beginWord, dist)])

        while que:
            word, dist = que.popleft()
            if word == endWord:
                return dist
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]

                    if next_word not in word_set:
                        continue
                    word_set.discard(next_word)
                    que.append((next_word, dist+1))

        return 0