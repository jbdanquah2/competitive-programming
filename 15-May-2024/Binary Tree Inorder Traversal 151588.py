# Problem: Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        result = []

        def inOrder(node):
            if node.left:
                inOrder(node.left)

            result.append(node.val)  
             
            if node.right:
                inOrder(node.right)
    

        inOrder(root)

        return result