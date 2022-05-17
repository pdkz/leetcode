class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses
        edges = []
        for i in range(numCourses):
            edges.append([])

        for pair in prerequisites:
            src, dst = pair
            edges[src].append(dst)
            indeg[dst] += 1

        ans = list(v for v in range(numCourses) if indeg[v] == 0)
        if not ans:
            return False

        deq = deque(ans)
        while deq:
            v = deq.popleft()
            for t in edges[v]:
                indeg[t] -= 1
                if indeg[t] == 0:
                    deq.append(t)
                    ans.append(t)

        return True if len(ans) == numCourses else False