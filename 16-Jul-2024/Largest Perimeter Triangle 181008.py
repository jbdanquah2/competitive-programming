# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if a < b + c:
                return a + b + c
        return 0
