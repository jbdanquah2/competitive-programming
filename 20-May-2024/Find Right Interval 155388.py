# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        
        def binary_search(target):
            left, right = 0, n - 1
            while left < right:
                mid = (left + right) // 2
                if starts[mid][0] < target:
                    left = mid + 1
                else:
                    right = mid
            return left if starts[left][0] >= target else -1
        
        result = []
        for interval in intervals:
            index = binary_search(interval[1])
            if index == -1:
                result.append(-1)
            else:
                result.append(starts[index][1])
        return result
        
            