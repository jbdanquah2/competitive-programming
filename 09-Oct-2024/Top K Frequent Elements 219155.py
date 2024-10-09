# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element
        count = Counter(nums)
        
        # Use a heap to keep track of the top k elements
        return heapq.nlargest(k, count.keys(), key=count.get)


        