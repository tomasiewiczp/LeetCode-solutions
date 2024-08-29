# problem url 
# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def removeElement(self, nums, val):
        """
        Removes all instances of 'val' from the list 'nums' in-place.
        
        Args:
        nums (List[int]): The list of integers from which we want to remove 'val'.
        val (int): The value to be removed from the list.

        Returns:
        int: The length of the modified list after removing all instances of 'val'.
        """
        k = 0  #  a pointer for the position to place the next valid element
        for i in range(len(nums)):
            if nums[i] != val:  
                nums[k] = nums[i] 
                k += 1  
        
        return k
