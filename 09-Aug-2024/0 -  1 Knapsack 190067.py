# Problem: 0 -  1 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    dp[i][w] = 0
                elif wt[i-1] <= w:
                    dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
                else:
                    dp[i][w] = dp[i-1][w]
    
        return dp[n][W]