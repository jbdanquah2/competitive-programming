# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0
        n = len(nums)
        
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                # Number of parts we can split nums[i] into to make it non-decreasing
                parts = (nums[i] + nums[i + 1] - 1) // nums[i + 1]
                operations += parts - 1
                
                # Update nums[i] to the maximum possible value that still fits in sequence
                nums[i] = nums[i] // parts
        
        return operations
            