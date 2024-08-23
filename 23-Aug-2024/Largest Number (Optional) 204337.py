# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        # Custom comparator function
        def compare(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1

        # Convert numbers to strings for comparison
        nums = list(map(str, nums))
        
        # Sort using the custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Concatenate the sorted numbers
        largest_num = ''.join(nums)
        
        # Handle the case where the result is multiple zeros (e.g., [0, 0])
        if largest_num[0] == '0':
            return '0'
        
        return largest_num
            