from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)-1):

            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

        for j in range(len(nums)):
            if nums[j] == 0:
                nums.remove(nums[j])
                nums.append(0)

        return nums
