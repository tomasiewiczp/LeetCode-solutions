# task url: https://leetcode.com/problems/plus-one/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for number,digit in enumerate(digits[::-1]):
            if digit != 9:
                digits[len(digits)-number-1]+=1
                return digits
            digits[len(digits)-number-1] = 0
        # if all numbers is 0 (was 999... befor adding) we need to add additional 1 at the beggining
        return [1] + digits
