# task url: https://leetcode.com/problems/reverse-bits/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f'{n:032b}'[::-1], 2)
        # f'{n:032b}' converts int into binary form with 32 bits 
        # if we wouldn't inform that it has to be 32 bits leading zero's would be lost
        #  then we reverse and converts back to int informing about binary form
