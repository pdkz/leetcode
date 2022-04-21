class Solution:
    def __init__(self):
        self.memo = collections.defaultdict(int)
        
    def climbStairs(self, n: int) -> int:
        self.memo[1] = 1
        self.memo[2] = 2
        
        return self.fib(n)
        
    def fib(self, n):
        if self.memo.get(n):
            return self.memo[n]
        
        self.memo[n] = self.fib(n-2) + self.fib(n-1)
        return self.memo[n]
