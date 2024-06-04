# Problem: Kth Symbol in Grammer - https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        if n == 1:
            return 0
    
        mid = 2**(n-1) // 2  # Calculate the midpoint of the row
        if k <= mid:
            return self.kthGrammar(n-1, k)  # If k is in the first half, recurse on the previous row
        else:
            return 1 - self.kthGrammar(n-1, k-mid) 


        