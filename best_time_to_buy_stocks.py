# task url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
#  O(n) complexity
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = inf
        max_value = 0
        diff = 0
        for price in prices:
            if price<min_value:
                min_value = price
            if price - min_value > diff:
                diff = price - min_value
        return diff
