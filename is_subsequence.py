# task url: https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150
# complexity O(s+t)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s in t:
            return True
        pointer = 0
        for sign in t:
            if sign == s[pointer]:
                pointer += 1
            if pointer == len(s):
                return True
        return False

# complexity O(s*t)
class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer = 0
        for sign in s:
            pointer = t.find(sign, pointer)+1
            if pointer == 0:
                return False
        return True
