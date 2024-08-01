# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Step 1: Create the adjacency list
        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        # Step 2: Perform topological sort using Kahn's algorithm (BFS)
        topo_order = []
        queue = deque([i for i in range(n) if indegree[i] == 0])
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 3: Compute ancestors using dynamic programming
        ancestors = [set() for _ in range(n)]
        
        for node in topo_order:
            for neighbor in graph[node]:
                # Update the ancestors of the neighbor
                ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)
        
        # Convert sets to sorted lists
        result = [sorted(list(ancestors[node])) for node in range(n)]
        
        return result

            