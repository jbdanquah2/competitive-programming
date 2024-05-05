# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        freq = {}
        count = 0

        # for i in range(len(nums)):

        #    for j in range(len(nums)):

        #     if i < j and j != i and nums[i] == nums[j]:
        #         count += 1
        
        # return count

        for i in range(len(nums)):

            if nums[i] in freq:
                count += freq[nums[i]]
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        return count