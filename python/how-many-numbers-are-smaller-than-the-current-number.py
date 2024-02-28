from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        size = len(nums)
        output = [0] * size

        for i in range(len(nums)):

            for j in range(len(nums)):

                if i != j and nums[j] < nums[i]:
                    output[i] += 1

        return output

