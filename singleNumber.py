#task url: https://leetcode.com/problems/single-number/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = 0
        for n in nums:
            unique  ^= n
        return unique
#Using XOR cancels out all paired numbers because identical numbers XORed together result in zero, leaving only the single unique element.
