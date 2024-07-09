# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-pile for pile in piles]
        heapify(max_heap)

        # print(max_heap)

        while k > 0:

            max_stones = -heapreplace(max_heap, max_heap[0] // 2)
            # heapify(max_heap)

            k -= 1

        return -sum(max_heap)