# Problem: E - Boxes Packing - https://codeforces.com/gym/500425/problem/E

def min_visible_boxes(n, box_sizes):
    from collections import Counter
    
    size_counts = Counter(box_sizes)
    
    max_frequency = max(size_counts.values())
    
    return max_frequency

n = int(input())
box_sizes = list(map(int, input().split()))

print(min_visible_boxes(n, box_sizes))
