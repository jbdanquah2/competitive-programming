# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self):
        self.parent = {}
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX
    
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}
        
        # Step 1: Build the Union-Find structure
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                uf.add(email)
                email_to_name[email] = name
                uf.union(first_email, email)
        
        # Step 2: Group emails by their root parent
        email_groups = defaultdict(list)
        for email in email_to_name:
            root_email = uf.find(email)
            email_groups[root_email].append(email)
        
        # Step 3: Sort and prepare the result
        merged_accounts = []
        for root_email, emails in email_groups.items():
            merged_accounts.append([email_to_name[root_email]] + sorted(emails))
        
        return merged_accounts

        