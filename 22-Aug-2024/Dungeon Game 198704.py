# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        m, n = len(dungeon), len(dungeon[0])
    
        # Initialize the DP table with infinity values
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # Set the bottom-right corner (princess's room) to the base case
        dp[m][n-1] = dp[m-1][n] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                min_health_on_exit = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, min_health_on_exit - dungeon[i][j])
        
        return dp[0][0]
            