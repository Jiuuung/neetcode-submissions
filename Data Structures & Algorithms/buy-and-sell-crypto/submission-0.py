class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        profit = 0
        for i in prices[1:]:
            profit = max(profit, i-min_buy)
            min_buy = min(min_buy, i)
        return profit