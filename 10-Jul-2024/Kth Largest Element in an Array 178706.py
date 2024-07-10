# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # min_heap = []

        # for num in nums:

        #     heappush(min_heap, num)

        #     # If the heap exceeds size k, remove the smallest element
        #     if len(min_heap) > k:
        #         heappop(min_heap)
           
        # # The smallest element in the heap is the kth largest element
        # return min_heap[0]

        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        # Iterate over the remaining elements
        for num in nums[k:]:
            # If the current element is larger than the smallest element in the heap
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)
        
        # The smallest element in the heap is the kth largest element
        return min_heap[0]
            