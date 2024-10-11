# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        
        for i in range(len(nums)):
            # Get the index corresponding to the current number
            index = abs(nums[i]) - 1
            
            # If the number at this index is negative, we've seen this number before
            if nums[index] < 0:
                duplicates.append(abs(nums[i]))
            else:
                # Otherwise, negate the number at this index to mark it as seen
                nums[index] = -nums[index]
        
        return duplicates

        