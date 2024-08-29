# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        # XOR the two numbers
        xor_result = x ^ y

        # Count the number of 1's in the binary representation of the XOR result
        distance = bin(xor_result).count('1')
        
        return distance