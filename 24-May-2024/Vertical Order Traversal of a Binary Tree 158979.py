# Problem: Vertical Order Traversal of a Binary Tree - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Dictionary to store the column indices and their corresponding nodes with rows
        column_table = defaultdict(list)
        
        # Queue for BFS traversal
        queue = deque([(root, 0, 0)])  # (node, row, col)
        
        while queue:
            node, row, col = queue.popleft()
            
            if node is not None:
                column_table[col].append((row, node.val))
                
                # Append left and right children to the queue with updated row and col values
                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))
        
        # Sort the dictionary by columns and sort the entries in each column by (row, value)
        sorted_columns = sorted(column_table.items())
        result = []
        
        for col, values in sorted_columns:
            # Sort by row first, and by value secondarily if rows are the same
            sorted_values = sorted(values, key=lambda x: (x[0], x[1]))
            result.append([val for row, val in sorted_values])

        print(result)
        
        return result
            