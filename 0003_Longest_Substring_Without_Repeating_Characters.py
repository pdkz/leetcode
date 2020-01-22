class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = collections.defaultdict(int)
        l = len(s)
        result_str = ''
        result_len = 0
        for i in range(l):
            chars.clear()
            for j in range(0,l-i):
                ch = s[i+j]
                if chars.get(ch):
                    break
                chars[ch] = 1
                word_str = s[i:i+j+1]
                word_len = len(word_str)
                if word_len > result_len:
                    result_str = word_str
                    result_len = word_len
        return result_len
