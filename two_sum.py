# problem url https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}

        for i, num in enumerate(nums):
            if (target-num) in lookup:
                first_index = lookup[target-num]
                return [first_index, i]
            lookup[num]=i
