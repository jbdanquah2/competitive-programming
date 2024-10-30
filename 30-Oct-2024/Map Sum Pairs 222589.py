# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = {}  # Store key-value pairs to manage updates

    def insert(self, key: str, val: int) -> None:
        # Calculate the difference if the key already exists
        diff = val - self.map.get(key, 0)
        # Update the key with the new value
        self.map[key] = val

        # Traverse and update Trie nodes with the diff
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.value += diff  # Update cumulative value at each node

    def sum(self, prefix: str) -> int:
        # Traverse to the node representing the prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0  # Prefix not found
            node = node.children[char]
        
        return node.value  # Return the cumulative value for the prefix
