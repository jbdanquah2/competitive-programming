from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        len_strs = len(strs)
        len_str = len(strs[0])

        result = 0

        for col in range(len_str):
            for row in range(1, len_strs):

                if strs[row][col] < strs[row - 1][col]:
                    result += 1
                    break

        return result
