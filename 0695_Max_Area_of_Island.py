class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0

        row, col = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs(y, x):
            dirs = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]

            queue = deque()
            queue.append((y, x))
            count = 0

            while queue:
                _y, _x = queue.popleft()
                for dy, dx in dirs:
                    adj_y, adj_x = _y + dy, _x + dx
                    if (adj_y in range(row)
                        and adj_x in range(col)
                        and grid[adj_y][adj_x]
                        and (adj_y, adj_x) not in visited):

                        count += grid[adj_y][adj_x]
                        visited.add((adj_y, adj_x))
                        queue.append((adj_y, adj_x))

            return count

        for y in range(row):
            for x in range(col):
                if grid[y][x] and (y, x) not in visited:
                    max_area = max(max_area, bfs(y, x))
        return  max_area