# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
    
        # Create a DP table initialized with the first row of the matrix
        dp = matrix[0][:]  # Copy the first row as the initial state of dp
        
        # Fill the DP table row by row
        for i in range(1, n):
            new_dp = [0] * n
            for j in range(n):
                # For each element in the current row, calculate the minimum path sum
                left = dp[j-1] if j > 0 else float('inf')
                middle = dp[j]
                right = dp[j+1] if j < n-1 else float('inf')
                new_dp[j] = matrix[i][j] + min(left, middle, right)
            dp = new_dp  # Update dp to the new row's results
        
        # The minimum sum of a falling path will be the minimum value in the last row
        return min(dp)


        