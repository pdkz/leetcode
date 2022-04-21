class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        total_profit = 0
        profit = float('-inf')
        min_price = prices[0]

        for i in range(1, N):
            if prices[i] > prices[i-1]:
                profit = max(prices[i] - min_price, profit)
                min_price = prices[i]
                total_profit += profit
                profit = 0
            else:
                min_price = min(min_price, prices[i])

        return total_profit