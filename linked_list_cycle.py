#  task url: https://leetcode.com/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150
# Tortoise and Hare algorithm 
#  Space complexity: O(1)
#  Time complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
