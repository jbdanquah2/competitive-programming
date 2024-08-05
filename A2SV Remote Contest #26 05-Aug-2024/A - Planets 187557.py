# Problem: A - Planets - https://codeforces.com/gym/540348/problem/A

def minimum_destruction_cost(test_cases):
    results = []
    
    for case in test_cases:
        n, c, orbits = case
        from collections import Counter
        orbit_counts = Counter(orbits)
        
        total_cost = 0
        for orbit, count in orbit_counts.items():
            total_cost += min(count, c)
        
        results.append(total_cost)
    
    return results

# Reading input
t = int(input())
test_cases = []

for _ in range(t):
    n, c = map(int, input().split())
    orbits = list(map(int, input().split()))
    test_cases.append((n, c, orbits))

# Get the result
results = minimum_destruction_cost(test_cases)

# Print the results
for result in results:
    print(result)
