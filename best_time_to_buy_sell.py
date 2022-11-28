class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        min_buy = prices[0]
        profit = 0
        for i in range(len(prices)):
            profit = max(prices[i] - min_buy, profit)
            min_buy = min(prices[i], min_buy)
        return profit