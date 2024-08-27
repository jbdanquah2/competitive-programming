# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        xor_all_numbers = 0
        xor_array_numbers = 0
        n = len(nums)
        
        for i in range(n + 1):
            xor_all_numbers ^= i
        
        for num in nums:
            xor_array_numbers ^= num
        
        return xor_all_numbers ^ xor_array_numbers


        