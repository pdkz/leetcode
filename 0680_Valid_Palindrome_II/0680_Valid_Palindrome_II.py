class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        count = 0
        while i < j:
            if s[i] != s[j]:
                return self.is_palindrome(s, i+1, j) or self.is_palindrome(s, i, j-1)
            i += 1
            j -= 1

        return True

    def is_palindrome(self, s, i, j):
        start = i
        end = j
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True