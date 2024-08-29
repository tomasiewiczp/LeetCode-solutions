#  task url: https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
#  Moore's Voting Algorithm then it's O(n) complexity and O(1) space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        candidate = 0
        voting = 0
        for num in nums:
            if voting == 0:
                candidate = num
            if num == candidate:
                voting +=1
                continue
            voting -=1
        return candidate
