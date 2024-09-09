# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            # Update twos first with bits that appeared twice
            twos |= ones & num
            # XOR num to ones to keep track of bits that appear once
            ones ^= num
            # Get the bits that appeared three times
            threes = ones & twos
            # Clear the bits that appeared three times from ones and twos
            ones &= ~threes
            twos &= ~threes
        return ones
        