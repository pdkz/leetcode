from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])
        min_x, max_x, min_y, max_y = 0, N-1, 0, M-1
        x, y, ans = 0, 0, []
        while min_x <= max_x and min_y <= max_y:
            for x in range(x, max_x+1):
                ans.append(matrix[y][x])
            y += 1
            min_y += 1

            for y in range(y, max_y+1):
                ans.append(matrix[y][x])
            x -= 1
            max_x -= 1

            if not (min_x <= max_x and min_y <= max_y):
                break

            for x in range(x, min_x-1,-1):
                ans.append(matrix[y][x])
            y -= 1
            max_y -= 1

            for y in range(y, min_y-1, -1):
                ans.append(matrix[y][x])
            x += 1
            min_x += 1
        return ans