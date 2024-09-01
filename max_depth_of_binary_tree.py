#  task url: https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=top-interview-150
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#  recursive, nice and clean solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_branch = self.maxDepth(root.left)
        right_branch = self.maxDepth(root.right)
        return 1+ max (left_branch,right_branch)

# BFS algorithm 
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0
        actual_row = [root]
        while actual_row:
            next_row = []
            for node in actual_row:
                if node.left:
                    next_row.append(node.left)
                if node.right:
                    next_row.append(node.right)
            actual_row.clear()
            actual_row.extend(next_row)
            depth += 1
        return depth
