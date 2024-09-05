# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = list(range(n + 1))
        rank = [1] * (n + 1)
        min_score = float('inf')

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            rootU = find(u)
            rootV = find(v)

            if rootU != rootV:
                if rank[rootU] > rank[rootV]:
                    parent[rootV] = rootU
                elif rank[rootU] < rank[rootV]:
                    parent[rootU] = rootV
                else:
                    parent[rootV] = rootU
                    rank[rootU] += 1

        for a, b, distance in roads:
            union(a, b)

        for a, b, distance in roads:
            if find(1) == find(a):
                min_score = min(min_score, distance)

        return min_score

        