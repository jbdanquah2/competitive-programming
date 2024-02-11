from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums_count = Counter(nums)

        return  [ key for key, value in nums_count.items() if value > len(nums) / 3]
