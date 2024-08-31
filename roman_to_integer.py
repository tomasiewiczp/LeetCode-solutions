#  task url: https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&envId=top-interview-150
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        maping_symbols = {
            'I' : 1
            , 'V' : 5
            , 'X' : 10
            , 'L' : 50
            , 'C' : 100
            , 'D' : 500
            , 'M' : 1000
        }
        final_number = 0

        for num, symbol in enumerate(s):
            if num < len(s)-1 and maping_symbols[symbol]< maping_symbols[s[num+1]]:
                final_number -= maping_symbols[symbol]
            else:
                final_number += maping_symbols[symbol]
        return final_number
