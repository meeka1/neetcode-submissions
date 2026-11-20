class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = selling_price - buying_price
        profit, max_profit = 0, 0

        for b in range(len(prices)):
            for s in range(b+1, len(prices)):
                profit = prices[s] - prices[b]
                max_profit = max(max_profit, profit)
            
        return max_profit