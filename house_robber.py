# task url: https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=top-interview-150
#  solution using DP algo
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Initialize the starting values:
        # prev1 - the maximum profit up to the current house (initially, it's the max of the first two houses)
        # prev2 - the maximum profit up to the previous house (initially, it's just the value of the first house)
        prev1 = max(nums[0:2])
        prev2 = nums[0] 
        for house_value in nums[2:]:
            # Calculate the maximum profit if you rob the current house:
            # Either you skip the current house and keep the max profit up to the previous one (prev1),
            # or you rob the current house, add its value to the max profit up to the house before the previous one (prev2 + house_value)
            res = max(prev1, prev2+house_value)
            prev2 = prev1
            prev1 = res
        return prev1
