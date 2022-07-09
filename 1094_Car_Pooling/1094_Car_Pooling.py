from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        M = 1001
        N, loc = len(trips), [0] * M

        for i in range(N):
            loc[trips[i][1]] += trips[i][0]
            loc[trips[i][2]] -= trips[i][0]

        passengers = 0
        for i in range(M):
            passengers += loc[i]
            if passengers > capacity:
                return False
        return True