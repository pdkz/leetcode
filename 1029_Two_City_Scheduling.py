class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key=lambda x: x[0] - x[1])
        N = len(costs)
        
        total = 0
        for i, cost in enumerate(costs):
            if i < N // 2:
                total += cost[0]
            else:
                total += cost[1]
        return total