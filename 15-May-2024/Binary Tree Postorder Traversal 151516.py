# Problem: Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []

        def postOrder(node):
            if node.left:
                postOrder(node.left)
            if node.right:
                postOrder(node.right)
            result.append(node.val)

        postOrder(root)

        return result

        # if not root:
        #     return []

        # stack = [root]
        # result = []

        # while stack:
        #     node = stack.pop()

            


        