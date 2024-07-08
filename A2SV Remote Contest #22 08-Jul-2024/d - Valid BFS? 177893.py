# Problem: d - Valid BFS? - https://codeforces.com/gym/533316/problem/d

def is_valid_bfs(n, edges, sequence):
    from collections import deque
    
    if sequence[0] != 1:
        return "No"
    
    # Construct graph
    graph = [set() for _ in range(n + 1)]
    for x, y in edges:
        graph[x].add(y)
        graph[y].add(x)
    
    # Create a dictionary to store the positions of each node in the sequence
    position = {sequence[i]: i for i in range(n)}
    
    # Initialize BFS
    queue = deque([1])
    visited = [False] * (n + 1)
    visited[1] = True
    
    index = 1
    
    while queue:
        v = queue.popleft()
        current_level = []
        
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                current_level.append(u)
        
        # Sort current level nodes by their order in the sequence using the position dictionary
        current_level.sort(key=lambda x: position[x])
        
        for u in current_level:
            if sequence[index] != u:
                return "No"
            index += 1
            queue.append(u)
    
    return "Yes"

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
sequence = list(map(int, input().split()))

print(is_valid_bfs(n, edges, sequence))

