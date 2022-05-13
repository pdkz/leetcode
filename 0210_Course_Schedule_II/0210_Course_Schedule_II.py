class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites and numCourses == 1:
            return [0]

        edges = []
        indeg = [0] * numCourses

        for i in range(numCourses):
            edges.append([])

        for pair in prerequisites:
            src, dst = pair
            edges[src].append(dst)
            indeg[dst] += 1

        ans = list(v for v in range(numCourses) if indeg[v] == 0)
        if not ans:
            return []

        que = deque(ans)

        while que:
            v = que.popleft()
            for t in edges[v]:
                indeg[t] -= 1
                if indeg[t] == 0:
                    que.append(t)
                    ans.append(t)


        return ans[::-1] if len(ans) == numCourses else []