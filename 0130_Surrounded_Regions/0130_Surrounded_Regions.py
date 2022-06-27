from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        M, N = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            nonlocal visited
            if r < 0 or r > M-1 or c < 0 or c > N-1:
                return
            if (r, c) in visited or board[r][c] == 'X':
                return

            visited.add((r,c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(M):
            for c in range(N):
                if board[r][c] == 'O' and (r == 0 or c == 0 or r == M-1 or c == N-1):
                    dfs(r,c)

        for r in range(M):
            for c in range(N):
                if r > 0 and r < M-1 and c > 0 and c < N-1 and board[r][c] == 'O' and not (r,c) in visited:
                    board[r][c] = 'X'
