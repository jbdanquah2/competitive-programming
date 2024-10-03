# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind()

        # Union stones by row and column
        for x, y in stones:
            uf.union(x, y + 10001)  # Offset y by a large number to distinguish rows and columns

        # The number of connected components is the number of unique roots
        unique_roots = len(set(uf.find(x) for x, y in stones))

        # The number of stones that can be removed is total stones - number of connected components
        return len(stones) - unique_roots


        