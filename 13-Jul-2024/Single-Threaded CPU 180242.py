# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indexed_tasks = [(tasks[i][0], tasks[i][1], i) for i in range(n)]
        
        # Sort tasks by enqueue time
        indexed_tasks.sort()
        
        result = []
        min_heap = []
        time = 0
        index = 0
        
        while len(result) < n:
            # Add all tasks that are available by the current time to the heap
            while index < n and indexed_tasks[index][0] <= time:
                heapq.heappush(min_heap, (indexed_tasks[index][1], indexed_tasks[index][2]))
                index += 1
            
            if min_heap:
                # Get the task with the smallest processing time (and smallest index in case of tie)
                processing_time, task_index = heapq.heappop(min_heap)
                result.append(task_index)
                time += processing_time
            else:
                # If there are no available tasks, jump to the next task's enqueue time
                time = indexed_tasks[index][0]
        
        return result
            