from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        def bfs(image, sr, sc, new_color):
            q = deque()
            visited = set()
            d = [[1,0], [-1,0], [0,1], [0,-1]]

            color = image[sr][sc]
            q.append((sr,sc))

            while q:
                row, col = q.popleft()
                visited.add((row, col))
                image[row][col] = new_color

                for nx, ny in d:
                    if (0 <= col+nx < n) and (0 <= row+ny < m) \
                    and image[row+ny][col+nx] == color \
                    and (row+ny, col+nx) not in visited:
                        q.append((row+ny, col+nx))
            return image

        def dfs(image, r, c, color, new_color, visited):
            if r < 0 or r > m-1 or c < 0 or c > n-1:
                return
            if image[r][c] != color or (r,c) in visited:
                return

            image[r][c] = new_color
            visited.add((r,c))

            dfs(image, r+1, c, color, new_color, visited)
            dfs(image, r-1, c, color, new_color, visited)
            dfs(image, r, c+1, color, new_color, visited)
            dfs(image, r, c-1, color, new_color, visited)

        #dfs(image, sr, sc, image[sr][sc], newColor, set())
        #return image

        return bfs(image, sr, sc, newColor)