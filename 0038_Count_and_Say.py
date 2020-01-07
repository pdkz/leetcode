class Solution:
    def countAndSay(self, n: int) -> str:
        seq = '1'
        if n == 1:
            return seq
        
        for i in range(n-1):
            count = 0
            prev = seq[0]
            tmp = ''
            for j in seq:
                if prev != j:
                    s = str(count) + prev
                    tmp += s
                    count = 0
                #print(i, seq, j, count, prev, tmp)
                count += 1
                prev = j

            tmp += str(count) + prev
            seq = tmp
 
        return seq
