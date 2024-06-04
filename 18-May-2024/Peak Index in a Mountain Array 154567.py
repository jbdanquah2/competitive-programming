# Problem: Peak Index in a Mountain Array - https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        left, right = 0, len(arr) - 1
        idx = 0

        while left < right:

            mid = left + (right - left) // 2
            curr = arr[mid]

            if curr > arr[mid + 1] and curr > arr[mid - 1]:
                idx = mid
                break
            elif curr < arr[mid + 1]:
                left = mid + 1
                idx = left
            else:
                right = mid - 1
                idx = right
            
        return idx
        