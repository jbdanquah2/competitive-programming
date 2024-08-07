# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1: 
            return 1
        if n == 2:
            return 1

        dp = []
        dp.append(0)
        dp.append(1)
        dp.append(1)
        
        for i in range(3, n+1):
            dp.append(sum(dp[-3:])) 


        return dp[-1]
        