# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node: TreeNode, low: float, high: float) -> bool:
            # Empty trees are valid BSTs
            if not node:
                return True
            
            if node.val <= low or node.val >= high:
                return False
            
            # Recursively validate the left and right subtrees
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        
        return validate(root, float('-inf'), float('inf'))
        