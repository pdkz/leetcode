class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        table = collections.defaultdict(int)
        nlen = len(s)
        substr = s[0]
        max_substr_length = len(substr)
        table[substr] = 0

        begin = 0
        end = 0

        while begin <= end and begin < nlen and end < nlen:
            v = table.get(s[end])
            if begin < end:
                if v != None and v >= 0:
                    for i in range(begin, v+1):
                        del table[s[i]]

                    begin = v + 1
                    substr = s[begin:end+1]
                    
                    table[s[begin]] = begin
                    table[s[end]] = end
                else:
                    substr += s[end]
                    table[s[end]] = end
            end += 1

            if len(substr) > max_substr_length:
                max_substr_length = len(substr)

        return max_substr_length
