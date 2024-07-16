# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # Select as many `1`s as possible
        ones_selected = min(numOnes, k)
        k -= ones_selected
        
        # Select as many `0`s as possible
        zeros_selected = min(numZeros, k)
        k -= zeros_selected
        
        # Select as many `-1`s as possible
        neg_ones_selected = min(numNegOnes, k)
        
        # Calculate the sum
        max_sum = ones_selected * 1 + zeros_selected * 0 + neg_ones_selected * -1
        
        return max_sum