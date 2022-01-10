class Solution:
    def fib(self, n: int) -> int:
        memo = dict()
        def dfs(n):
            nonlocal memo

            if n == 0:
                return 0
            if n == 1:
                return 1

            if memo.get(n):
                return memo[n]

            memo[n] = dfs(n-1) + dfs(n-2)

            return memo[n]

        return dfs(n)