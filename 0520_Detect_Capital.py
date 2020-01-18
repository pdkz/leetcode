class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper(): 
            return True
        elif word.islower(): 
            return True
        else:
            for i, w in enumerate(word):
                if i > 0 and w.isupper():
                    return False
            return True
