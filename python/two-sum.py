class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_dict = {}

        for i, num in enumerate(nums):

            diff = target - num

            if diff in nums_dict:
                return [nums_dict[diff], i]

            nums_dict[num] = i

        return []


solution = Solution()
print(solution.twoSum([2, 5, 1, 3], 4))