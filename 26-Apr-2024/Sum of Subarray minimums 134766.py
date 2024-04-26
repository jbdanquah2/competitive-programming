# Problem: Sum of Subarray minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        result = 0
        arr.append(0)  # Append 0 to the end of the array to handle remaining elements

        for i, num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                idx = stack.pop()
                left = idx - stack[-1] if stack else idx + 1
                right = i - idx
                result = (result + arr[idx] * left * right) % MOD
            stack.append(i)

        return result
            