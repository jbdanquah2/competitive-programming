# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

            # def backtrack(start, end):
            #     if start == end:
            #         # If we've reached the end, add the current permutation to the result
            #         result.append(nums[:])
            #     for i in range(start, end):
            #         # Swap the current element with the start element
            #         nums[start], nums[i] = nums[i], nums[start]
            #         # Recurse for the next part of the list
            #         backtrack(start + 1, end)
            #         # Backtrack by swapping the elements back
            #         nums[start], nums[i] = nums[i], nums[start]

            # result = []
            # backtrack(0, len(nums))

            # return result

        def backtrack(bitmask, current):
            if len(current) == len(nums):
                result.append(current[:])
                return
            for i in range(len(nums)):
                # Check if the ith bit is 0 (i.e., nums[i] is not used)
                if not (bitmask & (1 << i)):
                    # Include nums[i] in the permutation
                    backtrack(bitmask | (1 << i), current + [nums[i]])

        result = []
        backtrack(0, [])
        return result


            