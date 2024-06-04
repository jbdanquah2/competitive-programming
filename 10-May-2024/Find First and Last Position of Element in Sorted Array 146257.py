# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search(nums, target, left_flag):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > target or (left_flag and nums[mid] == target):
                    right = mid
                else:
                    left = mid + 1
            return left

        left_idx = binary_search(nums, target, True)
        right_idx = binary_search(nums, target, False) - 1

        if left_idx <= right_idx and nums[left_idx] == target:
            return [left_idx, right_idx]
        else:
            return [-1, -1]

            