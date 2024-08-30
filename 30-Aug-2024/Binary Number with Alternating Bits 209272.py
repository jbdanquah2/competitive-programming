# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # XOR n with n shifted right by 1
        xor_result = n ^ (n >> 1)
        # Check if the result + 1 is a power of two
        return (xor_result & (xor_result + 1)) == 0
        