# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n < 4 and n == 1:
            return True
        elif n < 4 and n != 1:
            return False

        return self.isPowerOfFour(n / 4)
        