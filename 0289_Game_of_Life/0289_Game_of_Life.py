from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        M, N = len(board), len(board[0])
        def generate_state(r, c, cand: List):
            nonlocal board
            dirs = [[-1, -1], # Left-Up
                    [0, -1],  # Left
                    [1, -1],  # Left-Bottom
                    [1, 0],   # Bottom
                    [1, 1],   # Right-Bottom
                    [0, 1],   # Right
                    [-1, 1],  # Right-Up
                    [-1, 0]]  # Up

            cells, live = [], 0
            for y, x in dirs:
                if r+y >= 0 and r+y < M and c+x >= 0 and c+x < N:
                    cells.append(board[r+y][c+x])
                    if board[r+y][c+x] == 1: live += 1

            if  (board[r][c] == 0 and live == 3) or \
                (board[r][c] == 1 and (live >= 4 or live <= 1)):
                cand.append((r,c))

        cand = []
        for r in range(M):
            for c in range(N):
                generate_state(r, c, cand)
        for r, c in cand:
            board[r][c] = 0 if board[r][c] == 1 else 1