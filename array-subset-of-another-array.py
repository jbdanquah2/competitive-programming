from collections import Counter

def isSubset( a1, a2, n, m):
    
    a1_count = Counter(a1)
    a2_count = Counter(a2)
    
    for ele, count in a2_count.items():
        if a1_count[ele] <count:
            return 'No'
    return 'Yes'
