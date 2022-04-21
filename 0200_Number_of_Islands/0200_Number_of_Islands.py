class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        row, col = len(grid), len(grid[0])
        visited = set()
        count = 0
        
        def bfs(y, x):
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            queue = deque([[y,x]])
            
            while queue:
                y, x = queue.popleft()
                for d in dirs:
                    if (y+d[0] in range(row) 
                        and x+d[1] in range(col)
                        and grid[y+d[0]][x+d[1]] == '1'
                        and not (y+d[0], x+d[1]) in visited):
                        visited.add((y+d[0], x+d[1]))
                        queue.append([y+d[0], x+d[1]])
        
        for y in range(row):
            for x in range(col):
                if grid[y][x] == '1' and not (y, x) in visited:
                    bfs(y, x)
                    count += 1
        return count