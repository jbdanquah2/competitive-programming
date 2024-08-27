# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:

        ans = [0] * (n + 1)

        for i in range(n + 1):

            ans[i] = ans[i // 2] + (i % 2)

        return ans

        