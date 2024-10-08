# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:

        bit_length = num.bit_length()
        
        mask = (1 << bit_length) - 1

        print(bin(num), ' | ',bin(mask))

        return num ^ mask
        