# Problem: Maximum Element After Decreasing and Rearranging - https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr.sort()

        arr[0] = 1
        
        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i - 1] + 1)
        
        return arr[-1]
            