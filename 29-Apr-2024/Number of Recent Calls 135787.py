# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

from collections import deque

class RecentCounter:

    def __init__(self):
        self.requests = deque()
        self.counter = 0
        

    def ping(self, t: int) -> int:
        self.requests.append(t)
        # self.counter += 1

        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
    
        return len(self.requests)


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)