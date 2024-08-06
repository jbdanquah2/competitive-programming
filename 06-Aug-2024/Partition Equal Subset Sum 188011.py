# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total_sum = sum(nums)
    
        # If the total sum is odd, we cannot partition it into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        n = len(nums)
        
        # Initialize a dp array of size (target + 1) with False
        dp = [False] * (target + 1)
        dp[0] = True  # There's always a way to form a sum of 0 (by choosing no elements)
        
        # Iterate over each number in the array
        for num in nums:
            # Update the dp array from right to left
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]