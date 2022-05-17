class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])
        visited = set()

        def dfs(i, j, word, k):
            nonlocal board
            if k == len(word):
                return True
            if (i, j) in visited:
                return False
            if i < 0 or i > M-1 or j < 0 or j > N-1 or board[i][j] != word[k]:
                return False
            
            visited.add((i,j))

            r = dfs(i+1, j, word, k+1) \
                or dfs(i-1, j, word, k+1) \
                or dfs(i, j+1, word, k+1) \
                or dfs(i, j-1, word, k+1)

            visited.remove((i, j))

            return r
        
        for i in range(0, M):
            for j in range(0, N):
                if board[i][j] == word[0]:
                    if len(word) == 1 or dfs(i, j, word, 0):
                        return True
                    visited.clear()
        return False