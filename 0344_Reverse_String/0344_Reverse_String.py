class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s) - 1
        r = n // 2 + 1
        for i in range(r):
            tmp = s[i]
            s[i] = s[n - i]
            s[n - i] = tmp
        
