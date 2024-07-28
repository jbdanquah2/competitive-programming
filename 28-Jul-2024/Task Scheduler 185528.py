# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)
        
        cooldown_queue = deque()
        
        time = 0
        
        while max_heap or cooldown_queue:
            time += 1
            
            if max_heap:
                count = heapq.heappop(max_heap) + 1 
                if count != 0: 
                    cooldown_queue.append((count, time + n))
            
            if cooldown_queue and cooldown_queue[0][1] == time:
                heapq.heappush(max_heap, cooldown_queue.popleft()[0])
        
        return time
            