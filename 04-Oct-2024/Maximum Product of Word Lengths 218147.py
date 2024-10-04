# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # Create a list to hold the bitmask and length of each word
        bitmasks = []
        lengths = []
        
        for word in words:
            bitmask = 0
            for char in word:
                bitmask |= (1 << (ord(char) - ord('a')))  # Set the bit for the character
            bitmasks.append(bitmask)
            lengths.append(len(word))
        
        max_product = 0
        n = len(words)
        
        # Check pairs of words
        for i in range(n):
            for j in range(i + 1, n):
                # Check if the two words share common letters
                if bitmasks[i] & bitmasks[j] == 0:  # No common letters
                    product = lengths[i] * lengths[j]
                    max_product = max(max_product, product)
        
        return max_product
            