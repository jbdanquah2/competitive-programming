# Problem: Find Bottom Left Tree Value - https://leetcode.com/problems/find-bottom-left-tree-value/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        # If root is None, return None
        if not root:
            return None

        # Initialize a queue for level-order traversal
        queue = deque([root])
        
        # Variable to store the leftmost value
        leftmost_value = root.val
        
        # Perform level-order traversal
        while queue:
            # Number of nodes in the current level
            level_size = len(queue)
            
            for i in range(level_size):
                # Pop the front node of the queue
                node = queue.popleft()
                
                # Update the leftmost value at the beginning of each level
                if i == 0:
                    leftmost_value = node.val
                
                # Add child nodes of the current node to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        # The leftmost value of the last level
        return leftmost_value
