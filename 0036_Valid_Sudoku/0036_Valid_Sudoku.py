class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        M, N = len(board), len(board[0])
        hashset = set()

        for i in range(0, M):
            for j in range(0, N):
                if board[i][j] in hashset: return False
                if board[i][j].isnumeric(): hashset.add(board[i][j])
            hashset.clear()

        for j in range(0, N):
            for i in range(0, M):
                if board[i][j] in hashset: return False
                if board[i][j].isnumeric(): hashset.add(board[i][j])
            hashset.clear()

        for offset_x in range(0,N,3):
            for offset_y in range(0,M,3):
                for i in range(0,3):
                    for j in range(0,3):
                        c = offset_x+j
                        r = offset_y+i
                        if board[r][c] in hashset: return False
                        if board[r][c].isnumeric(): hashset.add(board[r][c])
                hashset.clear()

        return True