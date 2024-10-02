# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

from typing import List

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        
        # First pass: process all equality equations
        for equation in equations:
            if equation[1] == '=':
                uf.union(equation[0], equation[3])
        
        # Second pass: check all inequality equations
        for equation in equations:
            if equation[1] == '!':
                if uf.find(equation[0]) == uf.find(equation[3]):
                    return False
            
        return True

        