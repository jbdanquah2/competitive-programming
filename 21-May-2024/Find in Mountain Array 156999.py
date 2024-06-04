# Problem: Find in Mountain Array - https://leetcode.com/problems/find-in-mountain-array/description/

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        def binary_search(mountain_arr, target, left, right):

            while left <= right:

                mid = left + (right - left) // 2
                curr = mountain_arr.get(mid)

                if curr == target:
                    return mid
                elif curr < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return -1

        n = mountain_arr.length()
        
        # Find the peak element index
        left, right = 0, n - 1
        while left < right:
            
            mid = left + (right - left) // 2
            mid_val = mountain_arr.get(mid)

            if mid_val < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        peak = left
        print('peak', peak)

        # Search in the ascending part
        result = binary_search(mountain_arr, target, 0, peak)
        if result != -1:
            return result
        
        # Search in the descending part
        result = binary_search(mountain_arr, target, peak + 1, n - 1)
        return result

