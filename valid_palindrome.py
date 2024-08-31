#  task url: https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150
# solution using re library to replace all not alnum characters
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_phrase = re.sub(r'[\W_]', '', s.lower())
        return clean_phrase == clean_phrase[::-1]
