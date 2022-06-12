class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans, max_step = [], numRows+(numRows-3)
        for i in range(numRows):
            next_step = max_step if i == 0 else 2*(i-1)+1
            prev_step = max_step if i == 0 or i == numRows-1 else max_step-1-next_step
            j, k = 0, 0
            j += i
            while j < len(s):
                ans.append(s[j])
                step = prev_step+1 if k % 2 == 0 else next_step+1
                j += step
                k += 1
        return ''.join(ans)