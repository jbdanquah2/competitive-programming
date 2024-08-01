# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
         # Step 1: Create the adjacency list and calculate indegrees
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1
        
        # Step 2: Initialize the queue with nodes that have no incoming edges
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        # Step 3: Perform topological sorting
        topo_order = []
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            
            # Reduce the indegree of each neighbor
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                # If indegree becomes zero, add it to the queue
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If topo_order contains all courses, return it; otherwise, return an empty list
        if len(topo_order) == numCourses:
            return topo_order
        else:
            return []
            