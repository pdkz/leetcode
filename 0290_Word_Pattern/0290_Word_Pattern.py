class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        to_pattern = {}
        to_word = {}
        
        for i, word in enumerate(words):
            ptn = pattern[i]
            if to_pattern.get(word) and to_word.get(ptn):
                if to_pattern.get(word) == ptn and to_word.get(ptn) == word:
                    continue
                return False
            else:
                if not to_word.get(ptn) and to_pattern.get(word) or \
                to_word.get(ptn) and not to_pattern.get(word):
                    return False
                else:
                    to_pattern[word] = ptn
                    to_word[ptn] = word
        return True
