class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        chars = ''
        for i in range(l):
            ch = s[i].lower()
            if ch.isalpha() or ch.isdecimal():
                chars += ch
        return chars == chars[::-1]
