class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums_rearranged = []
        nums_neg = []
        nums_pos = []

        for num in nums:
            if num < 0:
                nums_neg.append(num)
                continue
            nums_pos.append(num)

        for i in range(len(nums)/2):
            nums_rearranged.append(nums_pos[i])
            nums_rearranged.append(nums_neg[i])

        return nums_rearranged
