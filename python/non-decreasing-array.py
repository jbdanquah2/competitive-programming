class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        check = 0

        for i in range(len(nums)-1):

            if nums[i] > nums[i+1]:
                check += 1
                if i < 1 or nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
        
        return check <= 1
