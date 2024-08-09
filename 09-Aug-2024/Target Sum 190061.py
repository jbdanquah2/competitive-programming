# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
    
        # Check if target is achievable
        if (total_sum + target) % 2 != 0 or total_sum < abs(target):
            return 0
        
        # Determine the target subset sum
        subset_sum = (total_sum + target) // 2
        
        # Initialize DP array
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # There's one way to get a sum of 0: use no elements.
        
        # Fill DP array
        for num in nums:
            for i in range(subset_sum, num - 1, -1):
                dp[i] += dp[i - num]
        
        return dp[subset_sum]
            