#  task url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150
# Greedy Algorithm 
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for num, price in enumerate(prices):
            if num < len(prices)-1 and price < prices[num+1]:
                total_profit += prices[num+1] - price
        return total_profit
