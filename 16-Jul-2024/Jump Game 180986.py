# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # Initialize the furthest reachable position
        furthest = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current index is beyond the furthest reachable position, return False
            if i > furthest:
                return False
            
            # Update the furthest reachable position
            furthest = max(furthest, i + nums[i])
            
            # Early exit if we can already reach the last index
            if furthest >= len(nums) - 1:
                return True
        
        # If we complete the iteration, we can reach the last index
        return True
            