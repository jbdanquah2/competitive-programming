# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

from typing import List

class Solution:
    def heapify(self, nums: List[int], n: int, i: int):
        largest = i  # Initialize largest as root
        left = 2 * i + 1  # left = 2*i + 1
        right = 2 * i + 2  # right = 2*i + 2

        # If left child is larger than root
        if left < n and nums[left] > nums[largest]:
            largest = left

        # If right child is larger than the current largest
        if right < n and nums[right] > nums[largest]:
            largest = right

        # If the largest is not the root
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]  # Swap
            # Recursively heapify the affected sub-tree
            self.heapify(nums, n, largest)

    def heap_sort(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Build a maxheap (rearrange the array)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            # Swap the root (largest element) with the last element
            nums[i], nums[0] = nums[0], nums[i]
            # Heapify the reduced heap
            self.heapify(nums, i, 0)

        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.heap_sort(nums)
