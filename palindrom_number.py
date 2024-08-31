# task url: https://leetcode.com/problems/palindrome-number/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
