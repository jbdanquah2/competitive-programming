from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        freq = len(nums) / 3

        nums_count = Counter(nums)

        result_set = {key for key, value in nums_count.items() if value > freq}

        return  list(result_set)

