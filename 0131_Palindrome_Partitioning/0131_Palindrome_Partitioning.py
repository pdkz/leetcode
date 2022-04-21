class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtrack(s, res, [], 0)
        return res

    def backtrack(self, s, res, tmp, begin):
        if begin == len(s):
            res.append(tmp[:])
            return

        end = begin
        for i in range(end, len(s)):
            substr = s[begin:i+1]
            if self.is_palindrome(substr, 0, i-begin):
                tmp.append(substr)
                self.backtrack(s, res, tmp, i+1)
                tmp.pop()

    def is_palindrome(self, s, low, high):
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True