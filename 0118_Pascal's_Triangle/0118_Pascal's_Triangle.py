class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        p = []
        for i in range(1, numRows+1):
            _ = []
            for j in range(i):
                if j == 0 or j == i-1:
                    _.append(1)
                else:
                    _.append(p[i-2][j-1] + p[i-2][j])
            p.append(_)
        return p
