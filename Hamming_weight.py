#  problem url: https://leetcode.com/problems/number-of-1-bits/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def hammingWeight(self, n: int) -> int:
        return f'{n:b}'.count('1')
    # f'{n:b}' converts int to string format of binary representation
