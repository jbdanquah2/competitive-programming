# Problem: Maximum Width of Binary Tree - https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        max_width = 0
        queue = deque([(root, 0)])  # (node, index)

        while queue:
            level_length = len(queue)
            level_min_index = queue[0][1]  # Minimum index at the current level
            first_index = last_index = 0

            for i in range(level_length):
                node, index = queue.popleft()
                # Adjust the index to be relative to the level's minimum index to prevent overflow
                current_index = index - level_min_index
                if i == 0:
                    first_index = current_index
                if i == level_length - 1:
                    last_index = current_index
                if node.left:
                    queue.append((node.left, 2 * current_index + 1))
                if node.right:
                    queue.append((node.right, 2 * current_index + 2))

            current_width = last_index - first_index + 1
            max_width = max(max_width, current_width)

        return max_width


        

        

        


        