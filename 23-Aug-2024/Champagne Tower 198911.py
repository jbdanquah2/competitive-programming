# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Initialize a dp array where dp[i][j] is the amount of champagne in the jth glass of the ith row.
        dp = [[0] * (r + 1) for r in range(101)]
        
        # Pour all champagne into the topmost glass
        dp[0][0] = poured
        
        # Iterate over each row and each glass in that row
        for i in range(100):
            for j in range(i + 1):
                # If there's overflow
                if dp[i][j] > 1:
                    excess = dp[i][j] - 1
                    dp[i][j] = 1  # Current glass can only hold 1 cup
                    dp[i + 1][j] += excess / 2  # Distribute excess to the left-down glass
                    dp[i + 1][j + 1] += excess / 2  # Distribute excess to the right-down glass
        
        # Return the amount in the queried glass (ensure it's between 0 and 1)
        return min(1, dp[query_row][query_glass])
            