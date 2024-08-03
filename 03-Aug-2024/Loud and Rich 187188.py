# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

from collections import defaultdict

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        # Step 1: Build the graph
        graph = defaultdict(list)
        for u, v in richer:
            graph[v].append(u)
        
        # Step 2: Initialize the answer array with default values
        n = len(quiet)
        answer = list(range(n))
        
        # Step 3: DFS function to find the quietest person
        def dfs(node):
            if answer[node] == node:  # if it's still the default value
                min_quiet = quiet[node]
                quietest_person = node
                for neighbor in graph[node]:
                    candidate = dfs(neighbor)
                    if quiet[candidate] < min_quiet:
                        min_quiet = quiet[candidate]
                        quietest_person = candidate
                answer[node] = quietest_person
            return answer[node]
        
        # Step 4: Run DFS for each person
        for i in range(n):
            dfs(i)
        
        return answer
            