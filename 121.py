class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        m = prices[0]  
        for i in range(len(prices)):
            m = min(m, prices[i])  
            profit = prices[i] - m 
            if profit > max_profit:
                max_profit = profit
        return max_profit