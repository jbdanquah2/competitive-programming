# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
 
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        # Calculate the count of good numbers for even and odd positions
        even_count = pow(5, (n + 1) // 2, MOD)  # 5 options for even positions
        odd_count = pow(4, n // 2, MOD)  # 4 options for odd positions (2, 3, 5, 7)

        # Multiply the counts for even and odd positions to get the total count
        total_count = (even_count * odd_count) % MOD

        return total_count
                        
            