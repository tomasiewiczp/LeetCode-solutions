#  task url: https://leetcode.com/problems/sqrtx/?envType=study-plan-v2&envId=top-interview-150
# binary search approach
class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0
        min = 1
        max = x
        
        while True:
            new_test = min + (max-min)//2
            if x > new_test**2:
                min = new_test
            if x < new_test**2:
                max = new_test
            if x == new_test**2:
                return new_test
            if max-min <2:
                return min
