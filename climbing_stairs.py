# task url: https://leetcode.com/problems/climbing-stairs/?envType=study-plan-v2&envId=top-interview-150
# due to the fact that on  step number n we achive directly only from step n-1 or n-2 in a one way
# the answer will always be amout of possibilities to reach step n-1 plus amount of possibilities to reach step n-2
    def climbStairs(self, n: int) -> int:
        tab = list(range(4))
        for steps in range(3,n+1):
            tab.append(tab[steps]+tab[steps-1])
        return tab[n]

# recursion version ( exceedes time limit)
class Solution2:
    def climbStairs(self, n: int) -> int:
        if n<4:
            return n
        return self.climbStairs(n-1)+ self.climbStairs(n-2)
