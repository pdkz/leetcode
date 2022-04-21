class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = set()
        l, ans, N = 0, 0, len(s)

        for r in range(N):
            while s[r] in hashmap:
                hashmap.discard(s[l])
                l += 1
            hashmap.add(s[r])
            ans = max(ans, r-l+1)
        return ans
