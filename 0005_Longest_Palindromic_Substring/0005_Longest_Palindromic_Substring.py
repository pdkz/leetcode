class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        longest_substring = ''
        longest_length = 0
        
        for c in range(1, 2*N):
            if c % 2 == 0:
                left = c // 2 - 1
                right = c // 2
            else:
                left = c // 2
                right = c // 2
            
            while True:
                if (left >= 0 and left < N and right >=0 and right < N) is False or s[left] != s[right]:
                    left += 1
                    right -= 1
                    break
                    
                left -= 1
                right += 1
            
            l = right - left + 1
            if l > longest_length:
                longest_length = l
                longest_substring = s[left:right+1]
                
        return longest_substring
