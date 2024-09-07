# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # XOR of all elements
        xor_sum = 0
        for num in nums:
            xor_sum ^= num

        # Find the rightmost set bit
        rightmost_set_bit = xor_sum & -xor_sum

        # Partition the array into two groups and find the two unique numbers
        num1, num2 = 0, 0
        for num in nums:
            if num & rightmost_set_bit:
                num1 ^= num  # where the bit is set
            else:
                num2 ^= num  # where the bit is not set

        return [num1, num2]