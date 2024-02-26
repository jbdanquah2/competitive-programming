from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''

        for digit in digits:
            num += str(digit)

        num = str(int(num) + 1)

        return [int(d) for d in num]
