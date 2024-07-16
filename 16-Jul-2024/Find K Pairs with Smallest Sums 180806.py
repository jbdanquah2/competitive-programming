# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # If either nums1 or nums2 is empty, return an empty list
        if not nums1 or not nums2:
            return []

        # Min-heap to store the pairs and their sums
        min_heap = []
        
        # Initialize the heap with the first element of nums1 and all elements of nums2
        for j in range(min(k, len(nums2))):
            heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))
        
        # List to store the result
        result = []

        # Extract the smallest pairs from the heap
        while min_heap and len(result) < k:
            sum, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])

            # If there's a next element in nums1, add the new pair to the heap
            if i + 1 < len(nums1):
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
        
        return result

            