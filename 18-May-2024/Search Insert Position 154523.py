# Problem: Search Insert Position - https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:


        left, right = 0, len(nums) - 1
        idx = 0

        while left <= right:
            mid = left + (right - left) // 2

            print('mid', mid)
            idx = mid

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                idx = left
            elif nums[mid] > target:
                right = mid - 1
                idx = right

            idx = mid

            if nums[idx] < target:
                idx += 1
            
        return idx


        