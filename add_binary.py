# problem url:https://leetcode.com/problems/add-binary/submissions/1402233634/?envType=study-plan-v2&envId=top-interview-150
class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]
        # int(a,2) converts string to int informing that the number in string is saved in binary form
        # [2:] cuts off the beggining of binary number (0b)
